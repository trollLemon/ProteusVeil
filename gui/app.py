from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

def run():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("Proteus") 



    label = QLabel(win)
    label.setText("Proteus")
    label.move(50, 50)

    win.show()
    sys.exit(app.exec_())




