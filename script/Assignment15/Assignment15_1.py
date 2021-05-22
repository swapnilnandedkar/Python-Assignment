"""1.Design automation script which accept directory name and display checksum of all files.

    Usage : DirectoryChecksum.py “Demo”
    Demo is name of directory."""

from sys import *
import os
import log
import hashlib

# callback method
def errorHandler(extension_instance):
    print(extension_instance)
    exit()

def calculateFileChecksum(path, blockSize = 1024):
    fd = open(path,'rb')
    hobj = hashlib.md5()
    
    buffer = fd.read(blockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fd.read(blockSize)
    fd.close()
    return hobj.hexdigest()
        
    
def displayFileChecksumFromDirectory(directory):
    if os.path.isdir(directory):
        log.Logger.writeLog("\nFile name with there checksum")
        for folder, subFolder, filename in os.walk(directory,onerror = errorHandler):
            for file in filename:
                if not file.startswith('.'):
                    actualPath = os.path.join(folder,file)
                    checksum = calculateFileChecksum(actualPath)
                    log.Logger.writeLog("{} : {}".format(actualPath,checksum))
    else:
        print("{} it is not a directory or directory not found".format(directory))


def main():
    if len(argv) != 2:
        print("Insufficient Arguments !!!")
        exit()
    
    log.Logger.openLogFile();
    log.Logger.writeLog("Display File Checksum script")
    displayFileChecksumFromDirectory(argv[1])
    log.Logger.closeLogFile()

if __name__ == "__main__":
    main()
