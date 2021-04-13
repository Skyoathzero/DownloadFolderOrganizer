from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import analize as anal 
import sys
#path C:\Users\NABEL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\pyqt5_tools 
#path C:\Users\NABEL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\qt5_applications\Qt\bin
class FileAnalizer(QMainWindow):
    def __init__(self):
        super(FileAnalizer, self).__init__()
        self.setWindowTitle("Test")
        self.setGeometry(200,200,350,300)
        self.initUI()

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
