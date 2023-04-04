#VERSION2 : Setting up a separate class
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton 

class ButtonHolder(QMainWindow):
    def __init__ (self): #constructor of oop
        super().__init__()
        self.setWindowTitle("Button Holder App") #method of QMainWndow from inheritance
        button = QPushButton("Press Me!")

        #Set up the button as our central widget
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = ButtonHolder()
window.show() 
app.exec()