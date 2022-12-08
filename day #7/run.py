import sys
import re
import numpy as np
from typing import Iterable
#from collections import Iterable                            # < py38

def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x
def print_hi():

    less100kCounter = 0
    with open(sys.argv[1]) as f:
        commands = list(f.read().splitlines())

    dirsDict = {}
    currentDir = ''
    currentDirLs = False
    for command in commands:
        if '$ cd' in command:

            dirName = command.split()[2]
            if dirName == '..':
                continue
            dirsDict[dirName] = []
            currentDirLs = False
            pass
        elif 'dir' in command:
            if currentDirLs:
                dirsDict[dirName].append(command.split()[1])
            pass
        elif ' ls' in command:
            currentDirLs = True
            pass
        elif re.search("^\\d", command):

            if currentDirLs:
                fileSize = int(command.split()[0])
                dirsDict[dirName].append(fileSize)
            pass
        else:
            if currentDirLs:
                dirsDict[dirName].append(command)
            pass



    for dirsDictKey in dirsDict.keys():

        for index, dirsDictKeyElement in enumerate(dirsDict[dirsDictKey]):

            if re.search("^\\d+", str(dirsDictKeyElement)):
                pass
            else:

                dirsDict[dirsDictKey][index] = dirsDict[dirsDictKeyElement]

    print('dirsDict = ', dirsDict)

    for dirsDictKey in dirsDict.keys():
        if sum(list(flatten(dirsDict[dirsDictKey]))) <= 100000:
            less100kCounter += sum(list(flatten(dirsDict[dirsDictKey])))
        dirsDict[dirsDictKey] = list(flatten(dirsDict[dirsDictKey]))

    print('dirsDict = ', dirsDict)
    print('less100kCounter = ', less100kCounter)


if __name__ == '__main__':
    print_hi()


