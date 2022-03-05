from operator import mod
import os

def fileMod(directory):
    for root, dir, files in os.walk(directory):
        for filename in files:
            modtime = os.path.getmtime(filename)
            print('Filename: ' + filename +', Time Modified: ' + datetime.fromtimestamp(modtime))

def getUsers(filepath):
    modtime = os.path.getmtime(filepath)
    dateTime = datetime.fromtimestamp(modtime)
    current = datetime.timestamp(datetime.now())
    os.system('last -s ' + dateTime + ' -t ' + current)

def main():
    dir = input('Please input the target directory: ')
    fileMod(dir)
    filePath = input('Please input a target file path or input [r] to rerun the filemod with the same directory: ')
    if filePath == 'r':
        fileMod(dir)
    else:
        getUsers(filePath)
