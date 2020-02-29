# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from bluetooth import *
import threading
import sqlite3

class Ui_Formab:

    def __init__(self, key, user, pas, mac):
        self.key = key
        if user!="None" and pas!="None" and mac!="None":
            self.us = user
            self.pa = pas
            self.ma = mac
            connection  = sqlite3.connect("login1.db")
            c = connection.cursor()
            result = c.execute("Select * From USERS WHERE USERNAME = ? AND PASSWORD = ? AND MAC = ?",(self.us,self.pa,self.ma))
            rows = result.fetchall()
            if(len(rows) > 0):
                for row in rows:
                    print(row)
                    print(row[0], row[1], row[3], row[4])
                    self.f = row[4]
            # print(user)
            # print(pas)
            # print(mac)

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        print("enc"+file_name)
        try:
            with open(file_name, 'rb') as fo:
                plaintext = fo.read()
            enc = self.encrypt(plaintext, self.key)
            with open(file_name + ".enc", 'wb') as fo:
                fo.write(enc)
            os.remove(file_name)
        except Exception as e:
            print(e)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        print("dec"+file_name)
        try:
            if ".enc" != file_name[-4:]:
                # sa = sa + ".enc"
                file_name = file_name +".enc"
                print("If Encryption working"+file_name)
                with open(file_name, 'rb') as fo:
                    ciphertext = fo.read()
                dec = self.decrypt(ciphertext, self.key)
                with open(file_name[:-4], 'wb') as fo:
                    fo.write(dec)
                os.remove(file_name)
            else:
                print("Else Encryption working"+file_name)
                with open(file_name, 'rb') as fo:
                    ciphertext = fo.read()
                dec = self.decrypt(ciphertext, self.key)
                with open(file_name[:-4], 'wb') as fo:
                    fo.write(dec)
                os.remove(file_name)
        except Exception as e:
            print(e)


    def getAllFiles(self, line):
        dir_path = line
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self, line):
        dirs = self.getAllFiles(line)
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self, line):
        dirs = self.getAllFiles(line)
        for file_name in dirs:
            self.decrypt_file(file_name)

    entries = []
    n1 = []
    m1 = []
    n = []
    m = []
    t_f = ''
    m_mac = ''

    def find_device(self):
        def mac1():
            global entries
            global n1
            global m1
            entries = []
            n1 = []
            m1 = []
            self.listWidget.clear()
            print("performing inquiry...")

            nearby_devices = discover_devices(lookup_names = True)

            print("found %d devices" % len(nearby_devices))

            for name, addr in nearby_devices:
                print(" %s - %s" % (addr, name))
                entries.append(str(addr + " - " + name))
                m1.append(str(addr))
                n1.append(str(name))
            for i in entries:
                self.listWidget.addItem(i)

        try:
            threading.Thread(target=mac1).start()
        except Exception as e:
            print(e)

    def select(self):
        global n1
        global m1

        self.u_name_5.setText(n1[self.listWidget.currentRow()])
        self.u_name_6.setText(m1[self.listWidget.currentRow()])
        print(self.listWidget.currentItem().text())   
        
    
    def abc():
        def handshake():
            print(t_f)         
            global entries
            global n
            global m
            entries = []
            n = []
            m = []
            
            print("performing inquiry...")

            nearby_devices = discover_devices(lookup_names = True)

            print("found %d devices" % len(nearby_devices))

            for name, addr in nearby_devices:
                print(" %s - %s" % (addr, name))
                m.append(str(addr))
                n.append(str(name))
            if m_mac in n:
                print("Correct mac")
                # file = self.plainTextEdit_2.toPlainText()
                file = t_f
                for line in file.split("\n"):
                    print(line[8:], '   ', line[0:8])
                    if line[0:8] == 'file:///':
                        line = line[8:]
                    if os.path.isdir(line):
                        print("Folder")
                        enc.decrypt_all_files(line)
                    else:
                        enc.decrypt_file(line+".enc")
                        print("File")
                  
            else:
                print("Wrong mac")
                # file = self.plainTextEdit_2.toPlainText()
                file = t_f
                for line in file.split("\n"):
                    print(line[8:], '   ', line[0:8])
                    if line[0:8] == 'file:///':
                        line = line[8:]
                    if os.path.isdir(line):
                        print("Folder")
                        enc.encrypt_all_files(line)
                    elif os.path.isfile(line):
                        enc.encrypt_file(line)
                        print("File")
                
        while True:
            try:
                print("I am sleeping1")
                time.sleep(5)
                print("I am running1")
                threading.Thread(target=handshake).start()
            except Exception as e:
                print(e)
    try:
        print("I am sleeping1")         
        threading.Thread(target=abc).start()
        print("I am running1")
    except Exception as e:
        print(e)    

     # file = self.plainTextEdit_2.toPlainText()
     # for line in file.split("\n"):
     #   print(line[8:], '   ', line[0:8])
     #   if line[0:8] == 'file:///':
     #      line = line[8:]
     #       if os.path.isdir(line):
     #           print("Folder")
     #           enc.decrypt_all_files(line)
     #       elif os.path.isfile(line):
     #           enc.decrypt_file(line)
     #           print("File")


    def check_file(self):
        file = self.plainTextEdit_2.toPlainText()
        #print(file.readline())
        #print(file)
        # for line in file.split("\n"):
        #     print(line[8:], '   ', line[0:8])
        #     if line[0:8] == 'file:///':
        #         line = line[8:]
        #     if os.path.isdir(line):
        #         print("Folder")
        #         enc.encrypt_all_files(line)
        #     elif os.path.isfile(line):
        #         enc.encrypt_file(line)
        #         print("File")

    def update(self):
        connection  = sqlite3.connect("login1.db")
        username = self.u_name.toPlainText()
        password = self.u_name_2.toPlainText()
        mac = self.u_name_5.toPlainText()
        newusername = self.u_name_3.text()
        newpassword = self.u_name_4.text()
        newdevice = self.u_name_6.toPlainText()
        newmac = self.u_name_5.toPlainText()
        f_name = self.plainTextEdit_2.toPlainText()
        if username == self.us and password==self.pa:

            result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ? AND MAC = ?",(username,password,self.ma))
            if(len(result.fetchall()) > 0):
                connection.execute("UPDATE USERS SET USERNAME = ?, PASSWORD=?, DEVICE=?, MAC=?, FILE =? WHERE USERNAME = ? AND PASSWORD = ? AND  MAC=?",(newusername,newpassword,newdevice,newmac, f_name, username,password, mac));
                print("Update successfully")
                connection.commit()
            connection.close()

    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1030, 613)
        Form.setStyleSheet("background-color: rgb(43, 152, 189);")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(-3, 0, 1041, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(260, 20, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 500, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(61, 144, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(61, 177, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(80, 173, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")


        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(63, 229, 510, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")

        self.contact = QtWidgets.QLabel(self.tab)
        self.contact.setGeometry(QtCore.QRect(63, 363, 510, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.contact.setFont(font)
        self.contact.setStyleSheet("color: rgb(255, 255, 255);")
        self.contact.setObjectName("contact")


        self.no1 = QtWidgets.QLabel(self.tab)
        self.no1.setGeometry(QtCore.QRect(71, 415, 510, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.no1.setFont(font)
        self.no1.setStyleSheet("color: rgb(255, 255, 255);")
        self.no1.setObjectName("no1")

        self.no2 = QtWidgets.QLabel(self.tab)
        self.no2.setGeometry(QtCore.QRect(71, 448, 510, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.no2.setFont(font)
        self.no2.setStyleSheet("color: rgb(255, 255, 255);")
        self.no2.setObjectName("no3")

        self.no3 = QtWidgets.QLabel(self.tab)
        self.no3.setGeometry(QtCore.QRect(71, 481, 510, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.no3.setFont(font)
        self.no3.setStyleSheet("color: rgb(255, 255, 255);")
        self.no3.setObjectName("no3")

        self.no4 = QtWidgets.QLabel(self.tab)
        self.no4.setGeometry(QtCore.QRect(71, 514, 510, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.no4.setFont(font)
        self.no4.setStyleSheet("color: rgb(255, 255, 255);")
        self.no4.setObjectName("no4")


        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(71, 281, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(71, 314, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(90, 277, 500, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(90, 310, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.label_15 = QtWidgets.QLabel(self.Settings)
        self.label_15.setGeometry(QtCore.QRect(40, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Settings)
        self.label_16.setGeometry(QtCore.QRect(40, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Settings)
        self.label_17.setGeometry(QtCore.QRect(420, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Settings)
        self.label_18.setGeometry(QtCore.QRect(420, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Settings)
        self.label_19.setGeometry(QtCore.QRect(40, 190, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.u_name = QtWidgets.QTextEdit(self.Settings)
        self.u_name.setGeometry(QtCore.QRect(209, 52, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name.setFont(font)
        self.u_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.u_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name.setTabChangesFocus(True)
        self.u_name.setObjectName("u_name")
        self.dial = QtWidgets.QDial(self.Settings)
        self.dial.setGeometry(QtCore.QRect(220, 180, 50, 64))
        self.dial.setObjectName("dial")
        self.u_name_2 = QtWidgets.QTextEdit(self.Settings)
        self.u_name_2.setGeometry(QtCore.QRect(208, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name_2.setFont(font)
        self.u_name_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.u_name_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name_2.setTabChangesFocus(True)
        self.u_name_2.setObjectName("u_name_2")
        self.u_name_3 = QtWidgets.QLineEdit(self.Settings)
        self.u_name_3.setGeometry(QtCore.QRect(561, 52, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name_3.setFont(font)
        self.u_name_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.u_name_3.setObjectName("u_name_3")
        self.u_name_4 = QtWidgets.QLineEdit(self.Settings)
        self.u_name_4.setGeometry(QtCore.QRect(560, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name_4.setFont(font)
        self.u_name_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.u_name_4.setObjectName("u_name_4")
        self.u_name_5 = QtWidgets.QTextEdit(self.Settings)
        self.u_name_5.setEnabled(True)
        self.u_name_5.setGeometry(QtCore.QRect(843, 90, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name_5.setFont(font)
        self.u_name_5.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.u_name_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name_5.setTabChangesFocus(True)
        self.u_name_5.setReadOnly(True)
        self.u_name_5.setAcceptRichText(True)
        self.u_name_5.setObjectName("u_name_5")
        self.label_20 = QtWidgets.QLabel(self.Settings)
        self.label_20.setGeometry(QtCore.QRect(755, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.u_name_6 = QtWidgets.QTextEdit(self.Settings)
        self.u_name_6.setEnabled(True)
        self.u_name_6.setGeometry(QtCore.QRect(844, 52, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_name_6.setFont(font)
        self.u_name_6.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.u_name_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.u_name_6.setTabChangesFocus(True)
        self.u_name_6.setReadOnly(True)
        self.u_name_6.setAcceptRichText(True)
        self.u_name_6.setObjectName("u_name_6")
        self.label_21 = QtWidgets.QLabel(self.Settings)
        self.label_21.setGeometry(QtCore.QRect(755, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Settings)
        self.label_22.setGeometry(QtCore.QRect(546, 190, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.dial_2 = QtWidgets.QDial(self.Settings)
        self.dial_2.setGeometry(QtCore.QRect(846, 180, 50, 64))
        self.dial_2.setObjectName("dial_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.Settings)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(550, 261, 431, 181))
        self.plainTextEdit_2.setStyleSheet("background-color: white;")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.s_click_2 = QtWidgets.QPushButton(self.Settings)
        self.s_click_2.setGeometry(QtCore.QRect(676, 490, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.s_click_2.setFont(font)
        self.s_click_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.s_click_2.setObjectName("s_click_2")
        #######################################################
        self.s_click_2.clicked.connect(self.update)

        self.f_click = QtWidgets.QPushButton(self.Settings)
        self.f_click.setGeometry(QtCore.QRect(47, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.f_click.setFont(font)
        self.f_click.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.f_click.setObjectName("f_click")
        self.s_click_3 = QtWidgets.QPushButton(self.Settings)
        self.s_click_3.setGeometry(QtCore.QRect(212, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.s_click_3.setFont(font)
        self.s_click_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        #######################################################
        self.f_click.clicked.connect(self.find_device)

        self.s_click_3.setObjectName("s_click_3")
        self.listWidget = QtWidgets.QListWidget(self.Settings)
        self.listWidget.setGeometry(QtCore.QRect(37, 261, 301, 181))
        self.listWidget.setStyleSheet("background-color:\"white\"")
        self.listWidget.setAlternatingRowColors(False)
        #######################################################
        self.s_click_3.clicked.connect(self.select)

        self.listWidget.setObjectName("listWidget")
        self.line = QtWidgets.QFrame(self.Settings)
        self.line.setGeometry(QtCore.QRect(436, 173, 16, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.Settings, "")

        #######################################################
        print(self.us)
        print(self.pa)
        self.u_name.setText(self.us)
        # self.u_name_2.setText(self.pa)
        if self.f != "NULL":
            self.plainTextEdit_2.setPlainText(self.f)
            global t_f 
            t_f = self.f
        global m_mac
        m_mac = self.ma 


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Folder Secure"))
        self.label.setText(_translate("Form", "You are successfully login"))
        self.label_3.setText(_translate("Form", "Your files are now available for use"))
        self.label_7.setText(_translate("Form", "*"))
        self.label_8.setText(_translate("Form", "*"))
        self.label_9.setText(_translate("Form", "To Modify the Files, Folders or change username & Passward Tap on Settings"))
        self.label_10.setText(_translate("Form", "Warnings"))
        self.label_11.setText(_translate("Form", "*"))
        self.label_12.setText(_translate("Form", "*"))
        self.label_13.setText(_translate("Form", "Please don\'t Share your Password to anyone."))
        self.label_14.setText(_translate("Form", "Close your application before leave system"))
        self.contact.setText(_translate("Form", "Contact Us"))
        self.no1.setText(_translate("Form", "Krishna Kumar Singh - mymitedu.krishna@gmail.com"))
        self.no2.setText(_translate("Form", "Aachal Gupta        - aanchalgupta893@gmail.com"))
        self.no3.setText(_translate("Form", "Firoj Khan          - firojkhan84410@gmail.com"))
        self.no4.setText(_translate("Form", "Aman Singh          - amansinghdhanova@gmail.com"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Instructions"))
        self.label_15.setText(_translate("Form", "Current Username"))
        self.label_16.setText(_translate("Form", "Current Password"))
        self.label_17.setText(_translate("Form", "New Username"))
        self.label_18.setText(_translate("Form", "New Password"))
        self.label_19.setText(_translate("Form", "Choose Mac"))
        self.u_name.setPlaceholderText(_translate("Form", "Username"))
        self.u_name_2.setPlaceholderText(_translate("Form", "Password"))
        self.u_name_3.setPlaceholderText(_translate("Form", "Username"))
        self.u_name_4.setPlaceholderText(_translate("Form", "Password"))
        self.u_name_5.setPlaceholderText(_translate("Form", "MAC"))
        self.label_20.setText(_translate("Form", "Device"))
        self.u_name_6.setPlaceholderText(_translate("Form", "Device Name"))
        self.label_21.setText(_translate("Form", "MAC"))
        self.label_22.setText(_translate("Form", "Modify Files, Folders"))
        self.s_click_2.setText(_translate("Form", "Save Modifications"))
        self.f_click.setText(_translate("Form", "Find Devices"))
        self.s_click_3.setText(_translate("Form", "Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("Form", "Settings"))

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
us=''
ma=''
pa=''
enc = Ui_Formab(key, "None", "None", "None")

# def closeEvent(self, event):
#     file = t_f
#     print(file)
#     for line in file.split("\n"):
#         print(line[8:], '   ', line[0:8])
#         if line[0:8] == 'file:///':
#             line = line[8:]
#         if os.path.isdir(line):
#             print("Folder")
#             enc.encrypt_all_files(line)
#         elif os.path.isfile(line):
#             enc.encrypt_file(line)
#             print("File")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formab(key, "None", "None", "None")
    ui.setupUi(Form)
    Form.show()
    r = app.exec_()
    file = t_f
    print(file)
    for line in file.split("\n"):
        print(line[8:], '   ', line[0:8])
        if line[0:8] == 'file:///':
            line = line[8:]
        if os.path.isdir(line):
            print("Folder")
            enc.encrypt_all_files(line)
        elif os.path.isfile(line):
            enc.encrypt_file(line)
            print("File")
    sys.exit(r)



