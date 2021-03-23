from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import analize as anal 
import sys

# class FileAnalizer(QMainWindow):
#     def __init__(self)

def b1event():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,350,300)
    win.setWindowTitle("Test")

    label = QtWidgets.QLabel(win)
    label.setText("hello world")
    label.move(50,50   )

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Push Me")
    b1.clicked.connect(b1event)

    win.show()
    sys.exit(app.exec_())

window()
