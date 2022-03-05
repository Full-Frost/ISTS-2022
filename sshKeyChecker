import os
DIRECTORY = '/root/.ssh/'
keyFile = 'id_rsa'
def main():
    for root, dir, files in os.walk(DIRECTORY):
        for filename in files:
            if keyFile in filename:
                print('There are ssh keys present in the file directory')
            else:
                print('There are no ssh keys present')
