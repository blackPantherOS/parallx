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

class ParallX(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

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
