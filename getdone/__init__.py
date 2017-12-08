import os.path as osp

from getdone import GetDone as gd


def main():
    get_done_file = osp.expanduser('~/get-done')

    # Create empty file if it doesn't exist
    if not osp.exists(get_done_file):
        open(get_done_file, 'a').close()

    gd.toast("Hello")
