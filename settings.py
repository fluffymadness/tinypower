# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Thu Feb  6 16:00:36 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(402, 265)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.acpi = QtGui.QWidget()
        self.acpi.setObjectName(_fromUtf8("acpi"))
        self.formLayoutWidget = QtGui.QWidget(self.acpi)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 391, 151))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label)
        self.pButtonBox = QtGui.QComboBox(self.formLayoutWidget)
        self.pButtonBox.setObjectName(_fromUtf8("pButtonBox"))
        self.pButtonBox.addItem(_fromUtf8(""))
        self.pButtonBox.addItem(_fromUtf8(""))
        self.pButtonBox.addItem(_fromUtf8(""))
        self.pButtonBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pButtonBox)
        self.pbCommand = QtGui.QLineEdit(self.formLayoutWidget)
        self.pbCommand.setObjectName(_fromUtf8("pbCommand"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pbCommand)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_5)
        self.spButtonBox = QtGui.QComboBox(self.formLayoutWidget)
        self.spButtonBox.setObjectName(_fromUtf8("spButtonBox"))
        self.spButtonBox.addItem(_fromUtf8(""))
        self.spButtonBox.addItem(_fromUtf8(""))
        self.spButtonBox.addItem(_fromUtf8(""))
        self.spButtonBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.spButtonBox)
        self.spCommand = QtGui.QLineEdit(self.formLayoutWidget)
        self.spCommand.setObjectName(_fromUtf8("spCommand"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spCommand)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_6)
        self.ldClBox = QtGui.QComboBox(self.formLayoutWidget)
        self.ldClBox.setObjectName(_fromUtf8("ldClBox"))
        self.ldClBox.addItem(_fromUtf8(""))
        self.ldClBox.addItem(_fromUtf8(""))
        self.ldClBox.addItem(_fromUtf8(""))
        self.ldClBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.ldClBox)
        self.ldCommand = QtGui.QLineEdit(self.formLayoutWidget)
        self.ldCommand.setObjectName(_fromUtf8("ldCommand"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.ldCommand)
        self.tabWidget.addTab(self.acpi, _fromUtf8(""))
        self.dpms = QtGui.QWidget()
        self.dpms.setObjectName(_fromUtf8("dpms"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.dpms)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 401, 201))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_8.setIndent(2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.screenOffBattery = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.screenOffBattery.setObjectName(_fromUtf8("screenOffBattery"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.screenOffBattery)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_10.setIndent(2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.screenOffPlugged = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.screenOffPlugged.setObjectName(_fromUtf8("screenOffPlugged"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.screenOffPlugged)
        self.tabWidget.addTab(self.dpms, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Settings", None))
        self.label_2.setText(_translate("Dialog", "Power Button:", None))
        self.label.setText(_translate("Dialog", "Launch Command:", None))
        self.pButtonBox.setItemText(0, _translate("Dialog", "Hibernate", None))
        self.pButtonBox.setItemText(1, _translate("Dialog", "Nothing", None))
        self.pButtonBox.setItemText(2, _translate("Dialog", "Power Off", None))
        self.pButtonBox.setItemText(3, _translate("Dialog", "Suspend", None))
        self.label_3.setText(_translate("Dialog", "Suspend Key:", None))
        self.label_5.setText(_translate("Dialog", "Launch Command:", None))
        self.spButtonBox.setItemText(0, _translate("Dialog", "Hibernate", None))
        self.spButtonBox.setItemText(1, _translate("Dialog", "Nothing", None))
        self.spButtonBox.setItemText(2, _translate("Dialog", "Power off", None))
        self.spButtonBox.setItemText(3, _translate("Dialog", "Suspend", None))
        self.label_4.setText(_translate("Dialog", "Lid Close:", None))
        self.label_6.setText(_translate("Dialog", "Launch Command:", None))
        self.ldClBox.setItemText(0, _translate("Dialog", "Hibernate", None))
        self.ldClBox.setItemText(1, _translate("Dialog", "Nothing", None))
        self.ldClBox.setItemText(2, _translate("Dialog", "Power off", None))
        self.ldClBox.setItemText(3, _translate("Dialog", "Suspend", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acpi), _translate("Dialog", "Acpi", None))
        self.label_7.setText(_translate("Dialog", "On Battery :", None))
        self.label_8.setText(_translate("Dialog", "Screen off Time:", None))
        self.label_9.setText(_translate("Dialog", "On Power :", None))
        self.label_10.setText(_translate("Dialog", "Screen off Time:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dpms), _translate("Dialog", "DPMS", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

