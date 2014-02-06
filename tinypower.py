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
from PyQt4.QtCore import QSettings

ACPI_CMD = 'acpi'
BATTERYNAME = 'BAT0'
LIDOPEN = ''
ICONPATH = '/usr/share/pixmaps/tinypower/'

app = QtGui.QApplication(sys.argv)


class AppSettings():

    def __init__(self):
        self.settings = QSettings('tinypower', 'tinypower')

    def readSetting(self, settingsname):
        return self.settings.value(settingsname).toString()

    def readSettingInt(self, settingsname):
        if not self.settings.value(settingsname).toString():
           return 0
        else:
           return int(self.settings.value(settingsname).toString())

    def writeSetting(self, settingname, settingvalue):
        self.settings.setValue(settingname, settingvalue)


class SettingsExtended(settings.Ui_Dialog, QtGui.QDialog):
    def __init__(self):
        super(SettingsExtended, self).__init__()
        super(SettingsExtended, self).setupUi(self)

    def closeEvent(self, evnt):
        evnt.ignore()
        self.hide()


class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, parent=None):
        self.appSettings = AppSettings()
        self.settingsVar = SettingsExtended()
        self.batterychecker = BatteryChecker()
        self.acpichecker = AcpiEventChecker(self.appSettings)

        self.connect(self.batterychecker, QtCore.SIGNAL("setIcon"), self.set_icon)

        self.connect(self.settingsVar.buttonBox, QtCore.SIGNAL("accepted()"), self.saveSettings)
        self.connect(self.settingsVar.buttonBox, QtCore.SIGNAL("rejected()"), self.cancel)

        self.batterychecker.start()
        self.acpichecker.start()

        QtGui.QSystemTrayIcon.__init__(self, parent)
        self.set_icon('battery_full.png', '')
        self.menu = QtGui.QMenu(parent)

        configAction = self.menu.addAction("Config")
        configAction.triggered.connect(self.on_config)
        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(self.on_exit)
        self.setContextMenu(self.menu)

        self.dpms_init()

    def readSettings(self):
        self.settingsVar.ldCommand.setText(self.appSettings.readSetting('ldCommand'))
        self.settingsVar.pbCommand.setText(self.appSettings.readSetting('pbCommand'))
        self.settingsVar.spCommand.setText(self.appSettings.readSetting('spCommand'))
        self.settingsVar.pButtonBox.setCurrentIndex(self.appSettings.readSettingInt('pButtonBox'))
        self.settingsVar.spButtonBox.setCurrentIndex(self.appSettings.readSettingInt('spButtonBox'))
        self.settingsVar.ldClBox.setCurrentIndex(self.appSettings.readSettingInt('ldClBox'))
        self.settingsVar.screenOffBattery.setText(self.appSettings.readSetting('screenOffBattery'))
        self.settingsVar.screenOffPlugged.setText(self.appSettings.readSetting('screenOffPlugged'))

    def saveSettings(self):
        self.appSettings.writeSetting('ldCommand', self.settingsVar.ldCommand.text())
        self.appSettings.writeSetting('pbCommand', self.settingsVar.pbCommand.text())
        self.appSettings.writeSetting('spCommand', self.settingsVar.spCommand.text())
        self.appSettings.writeSetting('pButtonBox', self.settingsVar.pButtonBox.currentIndex())
        self.appSettings.writeSetting('spButtonBox', self.settingsVar.spButtonBox.currentIndex())
        self.appSettings.writeSetting('ldClBox', self.settingsVar.ldClBox.currentIndex())
        self.appSettings.writeSetting('screenOffBattery', self.settingsVar.screenOffBattery.text())
        self.appSettings.writeSetting('screenOffPlugged', self.settingsVar.screenOffPlugged.text())
        self.dpms_init()
        self.settingsVar.hide()

    def cancel(self):
        self.settingsVar.hide()

    def dpms_init(self):
        if self.batterychecker.checkIfPlugged():
            self.acpichecker.setDPMSPlugged()
        else:
            self.acpichecker.setDPMSBattery()

    def on_exit(self, event):
        self.batterychecker.stop()
        self.acpichecker.stop()
        sys.exit(1)

    def on_config(self, event):
        self.readSettings()
        self.settingsVar.show()

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


    def checkIfPlugged(self):
        text = subprocess.check_output(["acpi", "-V"]).strip('\n')
        if not 'off-line' in text:
            return True
        else:
            return False

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
    notification = pynotify.Notification("empty", "empty", "dialog-information")

    def __init__(self, appsettings):
        QtCore.QThread.__init__(self, parent=app)
        self.appsettings = appsettings

    def checkIfRunning(self, processname):
        p = subprocess.Popen(["pidof", "-x", processname], stdout=subprocess.PIPE)
        out, err = p.communicate()
        if len(out) > 0:
            return True
        else:
            return False

    def setDPMSPlugged(self):
        pluggedTime = self.appsettings.readSettingInt('screenOffPlugged')
        os.system('xset s off')
        os.system('xset +dpms')
        os.system('xset dpms'+' '+str(pluggedTime)+' '+str(pluggedTime)+' '+str(pluggedTime))

    def setDPMSBattery(self):
        batteryOffTime = self.appsettings.readSettingInt('screenOffBattery')
        os.system('xset s off')
        os.system('xset +dpms')
        os.system('xset dpms'+' '+str(batteryOffTime)+' '+str(batteryOffTime)+' '+str(batteryOffTime))

    # powerbutton, suspend key, lidclose
    # states: hibernate, nothing, poweroff, suspend
    def buttonCommand(self, buttonname):
        state = self.appsettings.readSettingInt(buttonname)
        print state
        if state == 0:
            os.system('systemctl hibernate')
        elif state == 2:
            os.system('systemctl poweroff')
        elif state == 3:
            os.system('systemctl suspend')

    def stop(self):
        self.running = 0

    def power_button(self):
        process = str(self.appsettings.readSetting('pbCommand'))
        if not self.checkIfRunning(process):
            self.buttonCommand('pButtonBox')
            os.system(process)

    def lid_open(self):
        print "not implemented yet"

    def lid_close(self):
        process = str(self.appsettings.readSetting('ldCommand'))
        if not self.checkIfRunning(process):
            self.buttonCommand('ldClBox')
            os.system(process)

    def button_sleep(self):
        process = str(self.appsettings.readSetting('spCommand'))
        if not self.checkIfRunning(process):
            self.buttonCommand('spButtonBox')
            os.system(process)


    def battery_charge(self):
        time.sleep(2)
        f = open('/sys/class/power_supply/'+BATTERYNAME+'/capacity')
        capacity = int(f.read(4096))
        f.close()

        return capacity

    def plugged(self):
        self.notification.update("Plugged", "Battery Status:"+str(self.battery_charge())+"%", "battery-plugged")
        self.notification.show()
        self.setDPMSPlugged()

    def unplugged(self):
        #notification=pynotify.Notification ("Unplugged","Battery remaining:","dialog-information")
        self.notification.update("Unplugged", "Battery Status:"+str(self.battery_charge())+"%", "battery-full")
        self.notification.show()
        self.setDPMSBattery()

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

