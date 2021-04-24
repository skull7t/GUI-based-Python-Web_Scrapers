# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Flip_Main.ui'
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

class Ui_FlipkartWindow(object):
       #
    def handleLogin(self):
        global g_url
        g_url=self.url.text()
        g_time=self.time.text()
        global g_email
        g_email=self.email.text()
        global g_number
        g_number=self.mobile.text()
        print(g_url)
        print(g_time)
        print(g_email)
        print(g_number)
        self.progressBar.setProperty("value", 20)
        with open('GITHUB/Flipkart_Main.csv', mode='w', newline="\n") as gvar:
               writer = csv.writer(gvar)
               writer.writerow([g_url])
               writer.writerow([g_email])
               writer.writerow([g_number])
               writer.writerow([g_time])
        self.progressBar.setProperty("value", 30)

    #
    def email_validator(self):
        is_valid = validate_email(email_address=g_email, check_regex=True, check_mx=True, from_address='my@from.addr.ess', helo_host='my.host.name', smtp_timeout=10, dns_timeout=10, use_blacklist=True, debug=False)
        global em
        if is_valid==True:
             print("email is valid")
             global em
             em = 1
             self.invalid_email.setVisible(False) 
             self.progressBar.setProperty("value", 50)
        else:
            em = 0
            print("Invalid email")
            self.invalid_email.setVisible(True) 
          
    #
    def url_validator(self):
        valid=validators. url(g_url)
        global ur
        if valid==True:
            print("Url is valid")
            global ur
            ur = 1
            self.invalid_url.setVisible(False) 
            self.progressBar.setProperty("value", 40)
        else:
            ur = 0
            print("Invalid url")
            self.invalid_url.setVisible(True) 
    #
    def number_validator(self):
        if re.match(r'[789]\d{9}$',g_number):   
            print("mobile no. is valid") 
            global nu
            nu = 1
            self.invalid_mobile.setVisible(False) 
            self.progressBar.setProperty("value", 60)
        else:  
            nu = 0
            print("Invalid mobile no.")
            self.invalid_mobile.setVisible(True) 



    def main(self):
        if em==1 & ur==1 & nu==1:
            print ('Starting Program')
            self.progressBar.setProperty("value", 100)
            FlipkartWindow.close()
            import flipkart_runcode
            exec(flipkart_runcode.py)
        else:
            print("all is invalid")
            self.progressBar.setProperty("value", 50)
            #MainWindow.close()
    #
    def setupUi(self, FlipkartWindow):
        FlipkartWindow.setObjectName("FlipkartWindow")
        FlipkartWindow.resize(1125, 621)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        FlipkartWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/71066a17509045338985457aa75f9137.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FlipkartWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FlipkartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.url_t = QtWidgets.QLabel(self.centralwidget)
        self.url_t.setGeometry(QtCore.QRect(340, 180, 401, 16))
        self.url_t.setObjectName("url_t")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(250, 230, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(340, 160, 481, 21))
        self.url.setPlaceholderText("")
        self.url.setObjectName("url")
        self.mobile = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile.setGeometry(QtCore.QRect(340, 410, 161, 22))
        self.mobile.setMaxLength(10)
        self.mobile.setObjectName("mobile")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(340, 360, 191, 22))
        self.email.setAutoFillBackground(False)
        self.email.setObjectName("email")
        self.time = QtWidgets.QLineEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(340, 220, 91, 41))
        self.time.setObjectName("time")
        self.time_t = QtWidgets.QLabel(self.centralwidget)
        self.time_t.setGeometry(QtCore.QRect(340, 260, 341, 20))
        self.time_t.setObjectName("time_t")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setGeometry(QtCore.QRect(250, 160, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_url.setFont(font)
        self.label_url.setObjectName("label_url")
        self.step1 = QtWidgets.QLabel(self.centralwidget)
        self.step1.setGeometry(QtCore.QRect(540, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.step1.setFont(font)
        self.step1.setObjectName("step1")
        self.submitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.submitbutton.setGeometry(QtCore.QRect(540, 490, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.submitbutton.setFont(font)
        self.submitbutton.setObjectName("submitbutton")
        self.submitbutton.clicked.connect(self.handleLogin)
        self.submitbutton.clicked.connect(self.url_validator)
        self.submitbutton.clicked.connect(self.email_validator)
        self.submitbutton.clicked.connect(self.number_validator)
        self.submitbutton.clicked.connect(self.main)
        self.step2 = QtWidgets.QLabel(self.centralwidget)
        self.step2.setGeometry(QtCore.QRect(540, 320, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.step2.setFont(font)
        self.step2.setObjectName("step2")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(250, 360, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.label_mobile = QtWidgets.QLabel(self.centralwidget)
        self.label_mobile.setGeometry(QtCore.QRect(250, 410, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_mobile.setFont(font)
        self.label_mobile.setObjectName("label_mobile")
        self.email_t = QtWidgets.QLabel(self.centralwidget)
        self.email_t.setGeometry(QtCore.QRect(340, 380, 341, 20))
        self.email_t.setObjectName("email_t")
        self.mobile_t = QtWidgets.QLabel(self.centralwidget)
        self.mobile_t.setGeometry(QtCore.QRect(340, 430, 341, 20))
        self.mobile_t.setObjectName("mobile_t")
        self.button_t = QtWidgets.QLabel(self.centralwidget)
        self.button_t.setGeometry(QtCore.QRect(470, 530, 231, 16))
        self.button_t.setObjectName("button_t")
        self.invalid_url = QtWidgets.QLabel(self.centralwidget)
        self.invalid_url.setGeometry(QtCore.QRect(870, 160, 91, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.invalid_url.setFont(font)
        self.invalid_url.setObjectName("invalid_url")
        self.invalid_url.setVisible(False) 
        self.invalid_email = QtWidgets.QLabel(self.centralwidget)
        self.invalid_email.setGeometry(QtCore.QRect(590, 360, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.invalid_email.setFont(font)
        self.invalid_email.setObjectName("invalid_email")
        self.invalid_email.setVisible(False) 
        self.invalid_mobile = QtWidgets.QLabel(self.centralwidget)
        self.invalid_mobile.setGeometry(QtCore.QRect(590, 410, 181, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.invalid_mobile.setFont(font)
        self.invalid_mobile.setObjectName("invalid_mobile")
        self.invalid_mobile.setVisible(False) 
        self.pricescraper_2 = QtWidgets.QLabel(self.centralwidget)
        self.pricescraper_2.setGeometry(QtCore.QRect(440, 70, 261, 31))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pricescraper_2.setFont(font)
        self.pricescraper_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pricescraper_2.setObjectName("pricescraper_2")
        self.icon_2 = QtWidgets.QLabel(self.centralwidget)
        self.icon_2.setGeometry(QtCore.QRect(410, 10, 341, 71))
        self.icon_2.setText("")
        self.icon_2.setPixmap(QtGui.QPixmap("../../Downloads/pngfind.com-flipkart-logo-png-3288902.png"))
        self.icon_2.setScaledContents(True)
        self.icon_2.setObjectName("icon_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(540, 550, 131, 23))
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        FlipkartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FlipkartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setObjectName("menubar")
        FlipkartWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FlipkartWindow)
        self.statusbar.setObjectName("statusbar")
        FlipkartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FlipkartWindow)
        QtCore.QMetaObject.connectSlotsByName(FlipkartWindow)

    def retranslateUi(self, FlipkartWindow):
        _translate = QtCore.QCoreApplication.translate
        FlipkartWindow.setWindowTitle(_translate("FlipkartWindow", "Flipkart_Scraper"))
        self.url_t.setText(_translate("FlipkartWindow", "*Copy the URL of the item from bowser, you want to scrape price of"))
        self.label_time.setText(_translate("FlipkartWindow", "Refresh time"))
        self.time.setPlaceholderText(_translate("FlipkartWindow", "   in minutes"))
        self.time_t.setText(_translate("FlipkartWindow", "*frequecy to check for data"))
        self.label_url.setText(_translate("FlipkartWindow", "URL"))
        self.step1.setText(_translate("FlipkartWindow", "STEP 1"))
        self.submitbutton.setText(_translate("FlipkartWindow", "SUBMIT"))
        self.step2.setText(_translate("FlipkartWindow", "STEP 2"))
        self.label_email.setText(_translate("FlipkartWindow", "Email ID"))
        self.label_mobile.setText(_translate("FlipkartWindow", "Mobile No."))
        self.email_t.setText(_translate("FlipkartWindow", "*Please input valid email ID to recive a price drop alert"))
        self.mobile_t.setText(_translate("FlipkartWindow", "*Please input valid email ID to recive a price drop alert"))
        self.button_t.setText(_translate("FlipkartWindow", "*A desktop Notification will also be sent"))
        self.invalid_url.setText(_translate("FlipkartWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">Invalid URL</span></p></body></html>"))
        self.invalid_email.setText(_translate("FlipkartWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">Invalid Email Id</span></p></body></html>"))
        self.invalid_mobile.setText(_translate("FlipkartWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">Invalid Mobile Number</span></p></body></html>"))
        self.pricescraper_2.setText(_translate("FlipkartWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">Price Scraper</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FlipkartWindow = QtWidgets.QMainWindow()
    ui = Ui_FlipkartWindow()
    ui.setupUi(FlipkartWindow)
    FlipkartWindow.show()
    sys.exit(app.exec_())