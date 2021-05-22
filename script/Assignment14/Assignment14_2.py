"""2. Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.
Usage : DirectoryRename.py “Demo” “.txt” “.doc”
Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc."""

from sys import *
import os

def validateExtension(extension):
    return extension.startswith('.') and len(extension)>1


# callback method
def errorHandler(extension_instance):
    print(extension_instance)
    exit()

def printApplicationStatistics(filescan,filextensionrename):
    print(" "*40,"Application Statistics")
    print(" "*36,"Total File Scanned : ",filescan)
    print(" "*36,"Total File extension renamed :",filextensionrename)
    

def renameFileExtension(file,srcExtension,destExtension):
    filename, filextension = os.path.splitext(file)
    if filextension == srcExtension:
        os.rename(file,filename + destExtension)
        return True
    return False



def DirectoryFileNameExtensionRename(directory, srcExtension, destExtension):
    filescan,filextensionrename = 0,0
    
    if validateExtension(srcExtension) and validateExtension(destExtension):
        for folder, subFolder, filename in os.walk(directory,onerror = errorHandler):
            for file in filename:
                filescan+=1
                actualpath = os.path.join(folder,file)
                if renameFileExtension(actualpath,srcExtension,destExtension):         # 0 : filename 1: extension name
                    filextensionrename+=1
    
    printApplicationStatistics(filescan,filextensionrename)
                


def main():
    if len(argv) != 4:
        print("Insufficient Arguments !!!")
        exit()
    
    DirectoryFileNameExtensionRename(argv[1], argv[2], argv[3])


if __name__ == "__main__":
    main()
