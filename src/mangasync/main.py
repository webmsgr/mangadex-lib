import argparse
import sys
import shlex
import mangadex

# Commands for the interface
# init <mangaid> <folder>: setup a folder to sync a manga, defaulting to sync all chapters
# addchapter <folder> <pattern>: add chapter(s) to sync
# sync <folder>: sync a folder
# removechapter <folder> <pattern>: remove chapter(s) to sync


try:
    import numpy as np
except ImportError:
    print(
        'This module requires extra requirements, install the extra "mangasync" to install these packages'
    )
    sys.exit(1)


def main():
    cmd = ""
    while cmd.lower() != "quit":
        cmd = input(">").lower()
        if cmd != "quit":
            pass
