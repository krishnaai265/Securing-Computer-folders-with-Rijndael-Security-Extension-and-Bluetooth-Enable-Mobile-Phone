# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import arrow_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(655, 496)
        Form.setStyleSheet("background-color: rgb(43, 152, 189);")
        self.c = QtWidgets.QPushButton(Form)
        self.c.setGeometry(QtCore.QRect(230, 330, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.c.setFont(font)
        self.c.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.c.setObjectName("c")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 40, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.u_name = QtWidgets.QTextEdit(Form)
        self.u_name.setGeometry(QtCore.QRect(170, 130, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name.setFont(font)
        self.u_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.u_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name.setTabChangesFocus(True)
        self.u_name.setObjectName("u_name")
        self.u_pass = QtWidgets.QTextEdit(Form)
        self.u_pass.setGeometry(QtCore.QRect(170, 200, 311, 31))
        self.u_pass.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.u_pass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_pass.setObjectName("u_pass")
        self.log_in = QtWidgets.QLabel(Form)
        self.log_in.setGeometry(QtCore.QRect(248, 447, 130, 20))
        self.log_in.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.log_in.setObjectName("log_in")
        self.c_pass = QtWidgets.QTextEdit(Form)
        self.c_pass.setGeometry(QtCore.QRect(170, 260, 311, 31))
        self.c_pass.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.c_pass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_pass.setObjectName("c_pass")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(356, 451, 21, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Folder Secure"))
        self.c.setText(_translate("Form", "Continue"))
        self.label.setText(_translate("Form", "Sign up"))
        self.u_name.setPlaceholderText(_translate("Form", "Username"))
        self.u_pass.setToolTip(_translate("Form", "Enter your Password"))
        self.u_pass.setPlaceholderText(_translate("Form", "Password"))
        self.log_in.setText(_translate("Form", "Already have account"))
        self.c_pass.setToolTip(_translate("Form", "Enter your Password"))
        self.c_pass.setPlaceholderText(_translate("Form", "Confirm password"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/arrow.png\" width=\"17\" height=\"12\"/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

