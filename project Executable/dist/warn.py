# -*- coding: utf-8 -*-

# Formwa implementation generated from reading ui file 'warn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formwawa(object):
    def close(self):
        import sys
        sys.exit(app.exec_())

    def setupUi(self, Formwa):
        Formwa.setObjectName("Formwa")
        Formwa.resize(468, 171)
        Formwa.setStyleSheet("background-color: rgb(43, 152, 189);")
        self.label_2 = QtWidgets.QLabel(Formwa)
        self.label_2.setGeometry(QtCore.QRect(172, -2, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Formwa)
        self.label_3.setGeometry(QtCore.QRect(129, 56, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
#        self.c_click = QtWidgets.QPushButton(Formwa)
#        self.c_click.setGeometry(QtCore.QRect(150, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
#        self.c_click.setFont(font)
#        self.c_click.setStyleSheet("background-color: rgb(255, 255, 255);\n"
#"color: rgb(0, 170, 255);")
#        self.c_click.setObjectName("c_click")
        ################################ mac ######################
#        self.c_click.clicked.connect(self.close)

        self.retranslateUi(Formwa)
        QtCore.QMetaObject.connectSlotsByName(Formwa)

    def retranslateUi(self, Formwa):
        _translate = QtCore.QCoreApplication.translate
        Formwa.setWindowTitle(_translate("Formwa", "Folder Secure"))
        self.label_2.setText(_translate("Formwa", "Invalid login"))
        self.label_3.setText(_translate("Formwa", "Incorrect UserName, Password, MAC"))
#        self.c_click.setText(_translate("Formwa", "OK"))

import arrow_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Formwa = QtWidgets.QWidget()
    ui = Ui_Formwawa()
    ui.setupUi(Formwa)
    Formwa.show()
    sys.exit(app.exec_())
