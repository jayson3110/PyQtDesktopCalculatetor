import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


#1, Create an instance of QApplication
# QApplication object(app) does so much initialization, you should create it
# before you create any other object related to the GUI
app = QApplication(sys.argv)

# 2. Create an instance of your application's GUI

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,280,80)
window.move(60,15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60,15)


#4.Show your application's GUI
window.show()

#5. Run your application's event loop(or main loop)
sys.exit(app.exec_())

