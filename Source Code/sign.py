# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from bluetooth import *
import threading
import sqlite3
import os
import sys


class Ui_Form1(object):

    entries = []
    n = []
    m = []

    def find_device(self):
        def mac1():
            global entries
            global n
            global m
            entries = []
            n = []
            m = []
            self.listWidget.clear()
            print("performing inquiry...")

            nearby_devices = discover_devices(lookup_names = True)

            print("found %d devices" % len(nearby_devices))

            for name, addr in nearby_devices:
                print(" %s - %s" % (addr, name))
                entries.append(str(addr + " - " + name))
                m.append(str(addr))
                n.append(str(name))
            #    entries = ['one','two', 'three']

            #model = QtGui.QStandardItemModel()
            #self.listView.setModel(model)

            #for i in entries:
            #    item = QtGui.QStandardItem(i)
            #    model.appendRow(item)
            for i in entries:
                self.listWidget.addItem(i)
        try:
        #    _thread.start_new_thread(mac1, () ) #("Thread-1", 2, )
            threading.Thread(target=mac1).start()
        except Exception as e:
            print(e)

    def select(self):
        global entries
        global n
        global m

        self.m_name.setText(n[self.listWidget.currentRow()])
        self.d_name.setText(m[self.listWidget.currentRow()])
        print(self.listWidget.currentItem().text())
        #print("selectedLayers = ",self.listView.currentIndex())
        #print("selectedLayers = ",self.listView.selectedIndexes())

    def signup(self):
        username = self.u_name.toPlainText()
        password = self.p_name.text()
        device = self.d_name.toPlainText()
        mac = self.m_name.toPlainText()
        import string
        ############################
        if any((char in string.punctuation for char in username) and (char in string.punctuation for char in password)):
            print("Invalid")
            ################################
            self.window = QtWidgets.QWidget()
            from warn import Ui_Formwawa
            self.ui = Ui_Formwawa()
            self.ui.setupUi(self.window)
            self.window.show()
            ################################
        else:
            print("Valid")
        ############################
            connection  = sqlite3.connect("login1.db")
            connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",(username,password,device,mac,"NULL"))
            connection.commit()
            connection.close()
            # Form.hide()
            # os.system("python login1.py")
            # sys.exit(app.exec_())
            # system.exit()
            print("Welcome to signup page")

    def sign(self):
        self.window = QtWidgets.QWidget()
        from login1 import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    #    self.login = QtGui.QMainWindow()
    #    self.ui = Ui_MainWindow()
    #    self.ui.setupUi(self.login)
    #    self.login.show()
        print("We are moving to sign page")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1030, 595)
        Form.setStyleSheet("background-color: rgb(43, 152, 189);")
        self.c_click = QtWidgets.QPushButton(Form)
        self.c_click.setGeometry(QtCore.QRect(690, 440, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.c_click.setFont(font)
        self.c_click.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.c_click.setObjectName("c_click")
        ################################ mac ######################
        self.c_click.clicked.connect(self.signup)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(690, 10, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.u_name = QtWidgets.QTextEdit(Form)
        self.u_name.setGeometry(QtCore.QRect(614, 139, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name.setFont(font)
        self.u_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.u_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name.setTabChangesFocus(True)
        self.u_name.setObjectName("u_name")

        self.p_name = QtWidgets.QLinetEdit(Form)
        self.p_name.setGeometry(QtCore.QRect(614, 209, 311, 31))
        self.p_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.p_name.setEchoMode(QtWidgets.QLineEdit.Password)
        self.p_name.setObjectName("p_name")
        
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(100, 50, 301, 401))
        self.listWidget.setStyleSheet("background-color:\"white\"")
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setObjectName("listWidget")
        self.f_click = QtWidgets.QPushButton(Form)
        self.f_click.setGeometry(QtCore.QRect(105, 500, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.f_click.setFont(font)
        self.f_click.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.f_click.setObjectName("f_click")
        ################################ mac ######################
        self.f_click.clicked.connect(self.find_device)

        self.s_click = QtWidgets.QPushButton(Form)
        self.s_click.setGeometry(QtCore.QRect(270, 500, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.s_click.setFont(font)
        self.s_click.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.s_click.setObjectName("s_click")
        ################################ mac ######################
        self.s_click.clicked.connect(self.select)

        self.d_name = QtWidgets.QTextEdit(Form)
        self.d_name.setGeometry(QtCore.QRect(616, 280, 311, 31))
        self.d_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.d_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.d_name.setUndoRedoEnabled(False)
        self.d_name.setReadOnly(True)
        self.d_name.setObjectName("d_name")
        self.m_name = QtWidgets.QTextEdit(Form)
        self.m_name.setGeometry(QtCore.QRect(617, 350, 311, 31))
        self.m_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.m_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.m_name.setUndoRedoEnabled(False)
        self.m_name.setReadOnly(True)
        self.m_name.setObjectName("m_name")
        self.a_click = QtWidgets.QPushButton(Form)
        self.a_click.setGeometry(QtCore.QRect(660, 510, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.a_click.setFont(font)
        self.a_click.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.a_click.setObjectName("a_click")
        ################################ mac ######################
        self.a_click.clicked.connect(self.sign)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Folder Secure"))
        self.c_click.setText(_translate("Form", "Continue"))
        self.label.setText(_translate("Form", "Sign up"))
        self.u_name.setPlaceholderText(_translate("Form", "Username"))
        self.p_name.setToolTip(_translate("Form", "Enter your Password"))
        self.p_name.setPlaceholderText(_translate("Form", "Password"))
        self.f_click.setText(_translate("Form", "Find Devices"))
        self.s_click.setText(_translate("Form", "Select"))
        self.d_name.setToolTip(_translate("Form", "Enter your Password"))
        self.d_name.setPlaceholderText(_translate("Form", "Device Name"))
        self.m_name.setToolTip(_translate("Form", "Enter your Password"))
        self.m_name.setPlaceholderText(_translate("Form", "MAC"))
        self.a_click.setText(_translate("Form", "Already have an Account"))

import arrow_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
