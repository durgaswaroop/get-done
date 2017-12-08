from PyQt5 import Qt
from playsound import playsound
import os

from getdone.Task import Task

GET_DONE_FILE_NAME = 'get-done'
GET_DONE_FILE_PATH = os.path.expanduser('~/' + GET_DONE_FILE_NAME)


def toast(msg):
    app = Qt.QApplication()
    notification = Qt.QSystemTrayIcon(Qt.QIcon('get_done.png'), app)
    notification.show()
    notification.showMessage("Get Done", msg)
    playsound('chime.mp3')


def save_task(task):
    create_gd_file_if_not_exists()
    with open(GET_DONE_FILE_PATH, 'a') as file:
        file.write(task.string_form() + os.linesep)


def create_gd_file_if_not_exists():
    # Create empty file if it doesn't exist
    if not os.path.exists(GET_DONE_FILE_PATH):
        open(GET_DONE_FILE_PATH, 'a').close()


def display_tasks():
    create_gd_file_if_not_exists()
    file = open(GET_DONE_FILE_PATH)
    lines = [line.strip() for line in file.readlines() if line.strip()]
    tasks = list(map(lambda s: Task.parse_string(s), lines))
    if len(tasks) == 0:
        print("No TODO's present")
        print("You are all caught up. Yay!")
        return
    file.close()
    # some processing here
    for task in tasks:
        print('TODO: ' + task.string_form())
