#!/usr/bin/env python2
#
# tinypower
# tidybatteryfork + acpi handling
# battery icons from faenza/faience
# @author fluffymadness
#
import subprocess
import time
import sys
import socket
import os
import pynotify
import settings
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QSettings, QString

ACPI_CMD = 'acpi'
BATTERYNAME = 'BAT0'
POWERBUTTON = 'oblogout'
BUTTONSLEEP = 'systemctl suspend; slimlock'	
LIDCLOSED = 'systemctl suspend; slimlock'
LIDOPEN = ''
ICONPATH = '/usr/share/pixmaps/tinypower/'

app = QtGui.QApplication(sys.argv)


class AppSettings():

    def __init__(self):
        self.settings = QSettings('tinypower', 'tinypower')

    def readSetting(self, settingsname):
        return self.settings.value(settingsname)


    def writeSetting(self, settingname, settingvalue):
        self.settings.setValue(settingname, settingvalue)


class SettingsExtended(settings.Ui_Dialog, QtGui.QDialog):
    def __init__(self, appsettings):
        self.appsettings = appsettings
        super(SettingsExtended, self).__init__()
        super(SettingsExtended, self).setupUi(self)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.saveSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.cancel)

        self.ldCommand.setText(self.appsettings.readSetting('ldCommand').toString())
        self.pbCommand.setText(self.appsettings.readSetting('pbCommand').toString())
        self.spCommand.setText(self.appsettings.readSetting('spCommand').toString())

    def showDialog(self):
        self.show()
        self.ldCommand.setText(self.appsettings.readSetting('ldCommand').toString())
        self.pbCommand.setText(self.appsettings.readSetting('pbCommand').toString())
        self.spCommand.setText(self.appsettings.readSetting('spCommand').toString())

    def saveSettings(self):
        self.hide()
        self.appsettings.writeSetting('ldCommand', self.ldCommand.text())
        self.appsettings.writeSetting('pbCommand', self.pbCommand.text())
        self.appsettings.writeSetting('spCommand', self.spCommand.text())

    def cancel(self):
        self.hide()

    def closeEvent(self, evnt):
        evnt.ignore()
        self.hide()


class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, parent=None):
        self.batterychecker = BatteryChecker()
        self.connect(self.batterychecker, QtCore.SIGNAL("setIcon"), self.set_icon)
        self.batterychecker.start()

        self.acpichecker = AcpiEventChecker()
        self.acpichecker.start()

        QtGui.QSystemTrayIcon.__init__(self, parent)
        self.set_icon('battery_full.png', '')
        self.menu = QtGui.QMenu(parent)

        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(self.on_exit)
        configAction = self.menu.addAction("Config")
        configAction.triggered.connect(self.on_config)

        self.appSettings = AppSettings()
        self.settingsVar = SettingsExtended(self.appSettings)

        self.setContextMenu(self.menu)

    def on_exit(self, event):
        self.batterychecker.stop()
        self.acpichecker.stop()
        sys.exit(1)

    def on_config(self, event):
        self.settingsVar.showDialog()

    def set_icon(self, trayicon, tooltip):
        icon = QtGui.QIcon(ICONPATH + trayicon +'.png')
        self.setToolTip(tooltip)
        self.setIcon(icon)


class BatteryChecker(QtCore.QThread):
    running = 1

    def __init__(self):
        QtCore.QThread.__init__(self, parent=app)

    def run(self):
        while self.running:
            info = self.get_battery_info()
            icon_name = self.get_icon_name(info['state'], info['percentage'])
            self.emit(QtCore.SIGNAL("setIcon"), icon_name, info['tooltip'])
            time.sleep(2)

    def stop(self):
        self.running = 0

    def get_battery_info(self):
        text = subprocess.check_output(ACPI_CMD).strip('\n')
        if not 'Battery' in text:
            return {'state':"Unknown",
                    'percentage':0,
                    'tooltip':""
                    }
        data = text.split(',')
        return {'state':data[0].split(':')[1].strip(' '),
                'percentage':int(data[1].strip(' %')),
                'tooltip': text.split(':',1)[1][1:]
        }

    def get_icon_name(self, state, percentage):
        if state == 'Discharging':
                if percentage < 10:
                        return 'battery_empty'
                elif percentage < 20:
                        return 'battery_caution'
                elif percentage < 40:
                        return 'battery_low'
                elif percentage < 60:
                        return 'battery_two_thirds'
                elif percentage < 75:
                        return 'battery_third_fouth'
                else:
                        return 'battery_full'
        elif state == 'Charged':
                return 'battery_charged'
        else:
                return 'battery_plugged'


class AcpiEventChecker(QtCore.QThread):
    running = 1
    pynotify.init("Hello world")
    notification = pynotify.Notification ("empty", "empty", "dialog-information")

    def __init__(self):
        QtCore.QThread.__init__(self, parent=app)

    def stop(self):
        self.running = 0

    def power_button(self):
        os.system(POWERBUTTON)

    def battery_charge(self):
        time.sleep(2)
        f = open('/sys/class/power_supply/'+BATTERYNAME+'/capacity')
        capacity = int(f.read(4096))
        f.close()

        return capacity

    def plugged(self):
        self.notification.update("Plugged", "Battery Status:"+str(self.battery_charge())+"%", "battery-plugged")
        self.notification.show()

    def unplugged(self):
        #notification=pynotify.Notification ("Unplugged","Battery remaining:","dialog-information")
        self.notification.update("Unplugged","Battery Status:"+str(self.battery_charge())+"%","battery-full")
        self.notification.show()

    def lid_open(self):
        os.system(LIDOPEN)

    def lid_close(self):
        os.system(LIDCLOSED)
    def button_sleep(self):
        os.system(BUTTONSLEEP)

    def brightness(self):
        f=open('/sys/class/backlight/acpi_video0/max_brightness')
        maxbrightness = float(f.read(4096))
        f.close()

        f=open('/sys/class/backlight/acpi_video0/actual_brightness')
        actualbrightness = float(f.read(4096))
        f.close()

        percent = (actualbrightness/maxbrightness)*100

        self.notification.update("Brightness",str(percent)+"%", "notification-display-brightness")
        self.notification.show()

    def run(self):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect("/var/run/acpid.socket")
        print "Connected to acpid"
        while self.running:
            for event in s.recv(4096).split('\n'):
                event = event.split(' ')
                if len(event)<2: continue
                    #print event
                if event[0]=='ac_adapter':
                    if event[3]=='00000001': #plugged
                        self.plugged() #Power plugged event
                    else: #unplugged
                        self.unplugged() #Power unplugged event
                elif event[0]=='button/power':
                    self.power_button() #Power button pressed
                elif event[0]=='button/lid':
                    if event[2]=='open':
                        self.lid_open() #Laptop lid opened
                    elif event[2]=='close':
                        self.lid_close() #Laptop lid closed
                elif event[0]=='button/sleep':
                    self.button_sleep()
                elif event[0]=='video/brightnessup':
                    self.brightness()
                elif event[0]=='video/brightnessdown':
                    self.brightness()

 
def main():
    trayIcon = SystemTrayIcon()
    trayIcon.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

