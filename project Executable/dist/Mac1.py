# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mac.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def mac(self):
        entries = ['one','two', 'three']

        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)

        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

                #        self.textEdit.setText(self.listView.selectedItem())
        #    print('selected item index found at %s with data: %s' % (model.row(), model.data().toString()))
        #    print("selectedLayers = ",self.listWidget.selectedItems())
#        print("selectedLayers = ",self.listView.currentIndex())

    def tex(self):
        self.textEdit.setText("Hello")
        print("selectedLayers = ",self.listView.currentIndex())
        print("selectedLayers = ",self.listView.selectedIndexes())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 30, 381, 401))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")
        ################################ mac ######################
        self.pushButton.clicked.connect(self.mac)
        #    self.listView.itemClicked.connect(self.ci)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(440, 190, 191, 31))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(250, 470, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        ################################ tex ######################
        self.pushButton1.clicked.connect(self.tex)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton1.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
