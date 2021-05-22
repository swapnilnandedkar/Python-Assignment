"""1.Design automation script which accept directory name and file extension from user. Display all
#files with that extension.
#Usage : DirectoryFileSearch.py “Demo” “.txt”
#Demo is name of directory and .txt is the extension that we want to search"""

from sys import *
import os

def validateExtension(extension):
    return extension.startswith('.') and len(extension)>1


# callback method
def errorHandler(extension_instance):
    print(extension_instance)
    exit()
    
def DirectoryFileSearchForExtension(directory, extension):
    if validateExtension(extension):
        for folder, subFolder, filename in os.walk(directory,onerror = errorHandler):
            for file in filename:
                if os.path.splitext(file)[1] == extension:
                    print(file)
                


def main():
    if len(argv) != 3:
        print("Insufficient Arguments !!!")
        exit()
    
    DirectoryFileSearchForExtension(argv[1], argv[2])


if __name__ == "__main__":
    main()
