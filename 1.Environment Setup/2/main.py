#Importing the components we need
from PySide6.QtWidgets import QApplication, QWidget

#The sys module is responsible for processing commmand line arguments
import sys

app = QApplication(sys.argv)

#by default QWidget is hidden
window = QWidget()

window.show()

#Start the event loop
app.exec()