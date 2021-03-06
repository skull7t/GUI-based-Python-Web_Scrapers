# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'content_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from validate_email import validate_email
import validators
import csv
import re

class Ui_ContentWindow(object):
    
    def handleLogin(self):
        global g_url
        g_url=self.url_txtbox.text()
        print(g_url)
        with open('GITHUB/Content_Main.csv', mode='w', newline='') as gvar:
               writer = csv.writer(gvar)
               writer.writerow([g_url])

    #
    def url_validator(self):
        valid=validators. url(g_url)
        global ur
        if valid==True:
            print("Url is valid")
            global ur
            ur = 1
            self.invalidmobile_label.setVisible(False) 
        else:
            ur = 0
            print("Invalid url")
            self.invalidmobile_label.setVisible(True)  
    #
    def main(self):
        if  ur==1 :
            print ('Starting Program')
            import content_runcode
            exec(content_runcode.py)
        else:
            print("all is invalid")
          

    def setupUi(self, ContentWindow):
        ContentWindow.setObjectName("ContentWindow")
        ContentWindow.resize(804, 481)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/71066a17509045338985457aa75f9137.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ContentWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ContentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.content_label = QtWidgets.QLabel(self.centralwidget)
        self.content_label.setGeometry(QtCore.QRect(250, 30, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setBold(False)
        font.setWeight(50)
        self.content_label.setFont(font)
        self.content_label.setObjectName("content_label")
        self.scraper_label = QtWidgets.QLabel(self.centralwidget)
        self.scraper_label.setGeometry(QtCore.QRect(340, 70, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setBold(False)
        font.setWeight(50)
        self.scraper_label.setFont(font)
        self.scraper_label.setObjectName("scraper_label")
        self.url_txtbox = QtWidgets.QLineEdit(self.centralwidget)
        self.url_txtbox.setGeometry(QtCore.QRect(220, 200, 381, 41))
        self.url_txtbox.setObjectName("url_txtbox")
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(370, 180, 55, 21))
        self.url_label.setObjectName("url_label")
        self.urldesc_label = QtWidgets.QLabel(self.centralwidget)
        self.urldesc_label.setGeometry(QtCore.QRect(280, 250, 231, 21))
        self.urldesc_label.setObjectName("urldesc_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(350, 310, 101, 28))
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.handleLogin)
        self.save_button.clicked.connect(self.url_validator)
        self.save_button.clicked.connect(self.main)
        self.invalidmobile_label = QtWidgets.QLabel(self.centralwidget)
        self.invalidmobile_label.setGeometry(QtCore.QRect(620, 210, 91, 16))
        self.invalidmobile_label.setObjectName("invalidmobile_label")
        self.invalidmobile_label.setVisible(False) 
        ContentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ContentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 26))
        self.menubar.setObjectName("menubar")
        ContentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ContentWindow)
        self.statusbar.setObjectName("statusbar")
        ContentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ContentWindow)
        QtCore.QMetaObject.connectSlotsByName(ContentWindow)

    def retranslateUi(self, ContentWindow):
        _translate = QtCore.QCoreApplication.translate
        ContentWindow.setWindowTitle(_translate("ContentWindow", "Content_Scraper"))
        self.content_label.setText(_translate("ContentWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ff0000;\">CONTENT</span></p></body></html>"))
        self.scraper_label.setText(_translate("ContentWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#000000;\">SCRAPER</span></p></body></html>"))
        self.url_label.setText(_translate("ContentWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">URL</span></p></body></html>"))
        self.urldesc_label.setText(_translate("ContentWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">*URL of the website to scrape</span></p></body></html>"))
        self.save_button.setText(_translate("ContentWindow", "SAVE TO HTML"))
        self.invalidmobile_label.setText(_translate("ContentWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">Invalid URL</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContentWindow = QtWidgets.QMainWindow()
    ui = Ui_ContentWindow()
    ui.setupUi(ContentWindow)
    ContentWindow.show()
    sys.exit(app.exec_())
