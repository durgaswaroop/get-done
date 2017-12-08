from PyQt5 import Qt
import sys
from playsound import playsound


def toast(msg):
    app = Qt.QApplication(sys.argv)
    notification = Qt.QSystemTrayIcon(Qt.QIcon('get_done.png'), app)
    notification.show()
    notification.showMessage("Get Done", msg)
    playsound('chime.mp3')


toast("Hello World")
