import argparse
import sys
import shlex
import mangadex
import threading
# Commands for the interface
# init <mangaid> <folder>: setup a folder to sync a manga, defaulting to sync all chapters
# addchapter <folder> <pattern>: add chapter(s) to sync
# sync <folder>: sync a folder
# removechapter <folder> <pattern>: remove chapter(s) to sync
# @todo add commands
# @body [ ] init  [ ] addchapter  [ ] sync  [ ] removechapter
class SyncedManga(mangadex.Manga):
    def __init__(self,id,remote=False):
        super().__init__(id,remote,False)
    def changes(self,changed,langcode="gb"):
        deleted = []
        changed = []
        added = []
        # @todo remove all chapters that dont fit the patterns
        for chapter in self.chapters:
            for lang in self.chapters[chapter]:
                if lang != langcode:
                    continue
                for num,group in enumerate(self.chapters[chapter][lang]):
                    try:
                        if not changed.chapters[chapter][lang][num] == group:
                            changed.append("{}:{}:{}".format(chapter,lang,num))
                    except IndexError:
                        deleted.append("{}:{}:{}".format(chapter,lang,num)) # @todo add added chapter
        return (deleted,changed,added)          
try:
    import numpy as np
except ImportError:
    print(
        'This module requires extra requirements, install the extra "mangasync" to install these packages'
    )
    sys.exit(1)
def helpcommand(_):
    print("""init <mangaid> <folder>: setup a folder to sync a manga, defaulting to sync all chapters
addchapter <folder> <pattern>: add chapter(s) to sync
sync <folder>: sync a folder
removechapter <folder> <pattern>: remove chapter(s) to sync""")
    return
def invalidcommand(_):
    print("invalid command")
    return

commands = {
"help":helpcommand
}
def main():
    cmd = ""
    while cmd.lower() != "quit":
        cmd = input(">").lower()
        if cmd != "quit":
            commandandargs = shlex.parse(cmd)
            command = commandandargs.pop(0)
            args = commandandargs
            commands.get(command,invalidcommand)(args)
            
