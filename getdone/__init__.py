from getdone import GetDone as gd
from getdone.Task import Task
import sys
from datetime import datetime


def main():
    # First argument is the name of the script file. So, ignoring it.
    default, args = sys.argv[0], sys.argv[1:]
    if len(args) == 0:
        gd.display_tasks()
    elif len(args) == 1 and args[0] == '-t':
        print("Get done: Incorrect Usage")
        print_usage()
    elif args[0] == '-t':
        if args[-1].casefold() != 'am' and args[-1].casefold() != 'pm':
            print("Get done: Incorrect Usage. AM/PM not specified")
            print_usage()
            return

        now = datetime.now()
        current_year = now.year
        current_month = now.month
        current_day = now.day

        # AM or PM will be the last value
        title = " ".join(args[1:-2])
        time_given = args[-2]

        hour, minute = parse_time(time_given)
        date = datetime(current_year, current_month, current_day, hour, minute)
        print(date)
        gd.save_task(Task(title, date))

    else:
        title = " ".join(args)
        gd.save_task(Task(title))


def parse_time(time_string):
    """
    Parses given time string to extract hour and minute.
    Eg: 11:34 -> 11,34
        11    -> 11,0
    :param time_string:
    :return: Tuple of hour and minute
    """
    if ":" in time_string:
        # Convert both to int from string
        hour, minute = tuple(map(int, time_string.split(":")))
    else:
        hour, minute = int(time_string), 0

    return hour, minute


def print_usage():
    print("""
    Usage:
       gd -t <task> <end-time> - Add task to TODO list with a time constraint
       gd <task>               - Add's task to TODO list
       gd                      - Display current tasks
       """.strip())
