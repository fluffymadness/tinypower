# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Thu Jan 23 15:13:24 2014
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
        Dialog.resize(394, 207)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 151))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
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
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label)

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Settings", None))
        self.label_2.setText(_translate("Dialog", "Power Button:", None))
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
        self.label.setText(_translate("Dialog", "Launch Command:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

