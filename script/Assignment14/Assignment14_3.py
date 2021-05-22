"""3. Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py “Demo” “Temp”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp."""

from sys import *
import os
import shutil
import log


# callback method
def errorHandler(extension_instance):
    print(extension_instance)
    exit()

def printApplicationStatistics(filecopy):
    log.Logger.writeLog("\n__________Application Statistics___________")
    print(" "*40,"Application Statistics")
    log.Logger.writeLog("Total File Copied : "+str(filecopy))
    print(" "*36,"Total File Copied : ",filecopy)
    

def copyDirectoryFile(srcdirectory, destdirectory):
    filecopy = 0
    try:
        if os.path.isdir(srcdirectory):
            os.mkdir(destdirectory)
            log.Logger.writeLog("\n_________Copied Files______________")
            for folder, subFolder, filename in os.walk(srcdirectory,onerror = errorHandler):
                for file in filename:
                    if(not file.startswith('.')):
                        actualpath = os.path.join(folder,file)
                        shutil.copy2(actualpath,destdirectory)
                        log.Logger.writeLog(file)
                        filecopy+=1
            
            printApplicationStatistics(filecopy)
        else:
            log.Logger.writeLog("Directory Not Found !!!")
            print("Directory Not Found !!!")
    except FileExistsError as e:
        log.Logger.writeLog("Error : {0} Directory already present !!!".format(destdirectory))
        print("Error : {0} Directory already present !!!".format(destdirectory))

def initialiseLog():
    log.Logger.openLogFile()
    
def main():
    initialiseLog()
    log.Logger.writeLog("Directory Traversal Script")
    
    if len(argv) != 3:
        print("Insufficient Arguments !!!")
        exit()
    
    copyDirectoryFile(argv[1], argv[2])


if __name__ == "__main__":
    main()
