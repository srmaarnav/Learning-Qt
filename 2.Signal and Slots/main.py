#VERSION3 : CAPTURE VALUE FROM A SLIDER - OTHER EXAMPLE
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

#The slot : responds when something happens
def respond_to_slider(data):
        print("slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(10)
slider.setValue(0)

#You just do the connection. The Qt system takes care of
#  passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
