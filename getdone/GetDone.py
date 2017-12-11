from PyQt5 import Qt
from playsound import playsound
import os
import threading

from getdone.Task import parse_string

GET_DONE_FILE_NAME = 'get-done'
GET_DONE_FILE_PATH = os.path.expanduser('~/' + GET_DONE_FILE_NAME)
THUMBS_UP = """
★░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░★ 
★░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░★ 
★░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░★ 
★░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░★ 
★░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░★ 
★░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░★ 
★░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░★ 
★░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░★ 
★░░░░░░░███████░░░░░░░██░░░░░░░░░░░░★ 
★░░░░█████░░░░░░░░░░░░░░███░██░░░░░░★ 
★░░░██░░░░░████░░░░░░░░░░██████░░░░░★ 
★░░░██░░████░░███░░░░░░░░░░░░░██░░░░★ 
★░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░★ 
★░░░░██████████░███░░░░░░░░░░░██░░░░★ 
★░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░★ 
★░░░░███████████░░██░░░░░░░░░░██░░░░★ 
★░░░░░░██░░░░░░░████░░░░░██████░░░░░★ 
★░░░░░░██████████░██░░░░███░██░░░░░░★ 
★░░░░░░░░░██░░░░░████░███░░░░░░░░░░░★ 
★░░░░░░░░░█████████████░░░░░░░░░░░░░★ 
★░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░★
"""


def toast(msg):
    """
    Show a simple toast message in the system tray popup.
    :param msg: Message to display
    :return: nothing
    """
    app = Qt.QApplication()
    notification = Qt.QSystemTrayIcon(Qt.QIcon('get_done.png'), app)
    notification.show()
    notification.showMessage("Get Done", msg)
    playsound('chime.mp3')


def save_task(task):
    """
    Saves the task to the GET_DONE_FILE_PATH.
    :param task: task to save to the file
    :return: nothing
    """
    create_gd_file_if_not_exists()
    with open(GET_DONE_FILE_PATH, 'a') as file:
        file.write(task.string_form() + os.linesep)
        print("Task '" + task.title + "' added")


def create_gd_file_if_not_exists():
    """
    Create empty file if it does not already exist.
    :return: nothing
    """
    if not os.path.exists(GET_DONE_FILE_PATH):
        open(GET_DONE_FILE_PATH, 'a').close()


def display_tasks():
    """
    Display existing tasks.
    :return: nothing
    """
    create_gd_file_if_not_exists()
    file = open(GET_DONE_FILE_PATH)
    lines = [line.strip() for line in file.readlines() if line.strip()]
    tasks = list(map(lambda s: parse_string(s), lines))
    if len(tasks) == 0:
        print("No TODO's present")
        print("You are all caught up. Yay!")
        return
    file.close()
    # some processing here
    max_length = str(len(max(tasks, key=lambda t: len(t.title)).title) + 5)
    for i, task in enumerate(tasks, start=1):
        if task.deadline:
            print(('{}: TODO: {:' + max_length + '} {} {}').format(str(i), task.title, 'Complete By:',
                                                                   str(task.deadline)))
        else:
            print(('{}: TODO: {:' + max_length + '}').format(str(i), task.title))
