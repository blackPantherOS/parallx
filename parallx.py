#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#*http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles K Barcza*
#*************************************************************************************(c)2002-2019********

import gettext
gettext.install("parallx", "/usr/share/locale")

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os, dbus

from parallx.ui_main import Ui_MainWindow
from parallx.fanout import Fanout

class ParallX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.goBtn.clicked.connect(self.goBtn_clicked)
        self.ui.addNewRemote.clicked.connect(self.addNewRemote_clicked)
        self.ui.editRemotePC.clicked.connect(self.editRemotePC_clicked)
        self.ui.delRemote.clicked.connect(self.delRemote_clicked)
        self.ui.testSshBtn.clicked.connect(self.testSshBtn_clicked)
        self.ui.exitBtn.clicked.connect(self.exitBtn_clicked)
        self.ui.repoUpdate.clicked.connect(self.repoUpdate_clicked)
        self.ui.rebootBtn.clicked.connect(self.rebootBtn_clicked)
        self.ui.ownCmd1.clicked.connect(self.ownCmd1_clicked)
        self.ui.ownCmd2.clicked.connect(self.ownCmd2_clicked)
        self.ui.installUpdate.clicked.connect(self.installUpdate_clicked)
        self.ui.shutDownBtn.clicked.connect(self.shutDownBtn_clicked)
        
    def shutDownBtn_clicked(self):
        print("shutDownBtn clicked")

    def installUpdate_clicked(self):
        print("installUpdate clicked")

    def goBtn_clicked(self):
        print("goBtn clicked")
        
    def addNewRemote_clicked(self):
        print("addNewRemote clicked")
        
    def editRemotePC_clicked(self):
        print("editRemotePC clicked")

    def delRemote_clicked(self):
        print("delRemote clicked")
    
    def testSshBtn_clicked(self):
        print("testSshBtn clicked")
        
    def exitBtn_clicked(self):
        print("exitBtn clicked")
        app.quit()
        
    def repoUpdate_clicked(self):
        print("repoUpdate clicked")

    def rebootBtn_clicked(self):
        print("rebootBtn clicked")
        
    def ownCmd1_clicked(self):
        print("ownCmd1 clicked")

    def ownCmd2_clicked(self):
        print("ownCmd2 clicked")

if __name__ == "__main__":

    homePage    = ""
    bugEmail    = ""

    aboutData   = ""
    
    if not dbus.get_default_main_loop():
        from dbus.mainloop.pyqt5 import DBusQtMainLoop
        DBusQtMainLoop(set_as_default = True)

    app = QApplication(sys.argv)
    window = ParallX()
    window.show()
    rect = QDesktopWidget().screenGeometry()
    window.move((rect.width()-window.width())//2, (rect.height()-window.height())//2)
    sys.exit(app.exec_())
