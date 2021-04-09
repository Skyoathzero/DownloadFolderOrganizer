from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import analize as anal 
import sys

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("hello world")
        self.label.move(50,50   )

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Push Me")
        self.b1.clicked.connect(self.b1event)
    def b1event(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):   
        self.label.adjustSize()
def b1event():
    print("clicked")


def window():
    app = QApplication(sys.argv)
    win = FileAnalizer()
    
    win.show()
    sys.exit(app.exec_())

window()
