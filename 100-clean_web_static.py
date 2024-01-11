#!/usr/bin/python3

"""
Fabric script to delete out-of-date archives.
The do_clean() function deletes old archives while keeping a specified number of recent archives.
It deletes local archives from the 'versions' folder, keeping the most recent.
It deletes remote archives from the '/data/web_static/releases' folder on the web servers, keeping the most recent.
The number argument specifies how many archives to keep. If 0 or 1, it keeps the most recent archive. If 2, it keeps the most recent and second most recent, etc.
"""

import os
from fabric.api import *

env.hosts = ['100.27.13.221', '54.210.79.93']


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
