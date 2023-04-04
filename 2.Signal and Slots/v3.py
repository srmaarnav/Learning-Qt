#VERSION1 : Just responding to the button click : syntax
from PySide6.QtWidgets import QApplication, QPushButton

#The slot : responds when something happens
def button_clicked(data):
        print("You clicked the button, didn't you! checked : ", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True) 
# Makes the button checkable, it is unchecked by default, i.e false, on clicking, it chages its state constantly, i.e.
# Makes further click toggle between check and uncheck

#clicked is a signal of QPushButton. It's emitted when you click on the button
#You can wire a slot to the signal using the syntax below : 
button.clicked.connect(button_clicked)

button.show()
app.exec()