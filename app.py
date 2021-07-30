# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import importlib
import os
import app1
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(440, 400)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 150, 221, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 330, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.generatepass)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 250, 321, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FIRST NAME:"))
        self.lineEdit.setStatusTip(_translate("MainWindow", "enter first name"))
        self.label_2.setText(_translate("MainWindow", "LAST NAME:"))
        self.lineEdit_2.setStatusTip(_translate("MainWindow", "enter last name"))
        self.pushButton.setText(_translate("MainWindow", "Check"))
        self.pushButton_2.setText(_translate("MainWindow", "Log In"))
        self.label_3.setText(_translate("MainWindow", "Password"))


    def get(self):
        fn = self.lineEdit.text()
        ln = self.lineEdit_2.text()
        print(fn)
        print(ln)
        import sqlite3
        db = sqlite3.connect("idpass.db")
        cur = db.cursor()
        checkfname = "select fname from idpass"
        cur=db.cursor()
        cur.execute(checkfname)
        fname = cur.fetchone()
        print(fname[0])
        checklname = "select [lname ] from idpass"
        cur=db.cursor()
        cur.execute(checklname)
        lname = cur.fetchone()
        print(lname[0])
        if fname[0] == fn:
            if lname[0] == ln:
                self.valid = "YOU ARE OWNER" 
                self.lineEdit_3.setText(self.valid)
        
        else:
            self.Try = "you are not authorized"
            self.lineEdit_3.setText(self.Try)


    def generatepass(self):
        import sqlite3
        db = sqlite3.connect("idpass.db")
        cur = db.cursor()
        pswd = self.lineEdit_4.text()
        print(pswd)
        checkpswd = "select password from idpass"
        cur = db.cursor()
        cur.execute(checkpswd)
        password = cur.fetchone()
        print(password[0])
        if(pswd == password[0]):
            os.system('python app1.py')
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
