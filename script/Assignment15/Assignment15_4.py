"""4. Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory. Display execution time required for the
script.
Usage : DirectoryDusplicateRemoval.py “Demo”
Demo is name of directory."""

from sys import *
import os
import log
import hashlib
import time

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


def logDuplicateFiles(similarChecksumdict):
    keys = similarChecksumdict.keys()
    
    for key in keys:
        similarFiles = similarChecksumdict.get(key)
        if len(similarFiles) > 1:
            log.Logger.writeLog("\nFilename : {}".format(similarFiles[0]))
            log.Logger.writeLog("Deleted Duplicates files")
            similarFiles.pop(0)
            for filename in similarFiles:
                os.remove(filename)
                log.Logger.writeLog(filename)
  
  
def displayFileChecksumFromDirectoryForSimilarFile(directory):
    if os.path.isdir(directory):
        log.Logger.writeLog("\nSimilar Files with there checksum")
        similarChecksumdict = {}
        
        for folder, subFolder, filename in os.walk(directory,onerror = errorHandler):
            for file in filename:
                if not file.startswith('.'):
                    actualPath = os.path.join(folder,file)
                    checksum = calculateFileChecksum(actualPath)
                    
                    if checksum in similarChecksumdict:
                        similarChecksumdict[checksum].append(actualPath)
                    else:
                        similarChecksumdict[checksum] = [actualPath]
                    
        logDuplicateFiles(similarChecksumdict)
    else:
        print("{} it is not a directory or directory not found".format(directory))


def main():
    if len(argv) != 2:
        print("Insufficient Arguments !!!")
        exit()
    
    log.Logger.openLogFile();
    log.Logger.writeLog("Display File Checksum script")
    displayFileChecksumFromDirectoryForSimilarFile(argv[1])
    log.Logger.closeLogFile()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- Execution time for script is %s seconds ---" % (time.time() - start_time))
