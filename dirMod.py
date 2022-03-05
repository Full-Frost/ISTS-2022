from datetime import datetime
from operator import mod
import os

def dirMod(directory):
    for root, dir, file, in os.walk(dir):
        for dirs in dir:
            modTime = os.path.getmtime(dir)
            print('Dir: ' + dir + ', Time Modified: ' + datetime.fromtimestamp(modTime))
            
def main():
    dir = '/'
    while(1):
        dirMod(dir)
