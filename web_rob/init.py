from selenium import webdriver
from selenium.webdriver.support.ui import Select
from rob1 import Rob
import sys
from PyQt4 import QtGui, QtCore
from err_window import Err_Window

DICT = {
        'amount': 4000,
        'durat': 30,
        'firstname': 'Vasya',
        'lastname': 'Pupkin',
        'mob_number': '3350090',
        'email': 'xxx@xxx.xx',
        'ch1': True,
        'ch2': True,
        }

browser = webdriver.Firefox()
browser.get("http://bbpujcka.cz/")
app = QtGui.QApplication(sys.argv)
Rob(DICT, browser)
#tg = Err_Window("ddddddddddd")
#tg.show()
#app.exec()