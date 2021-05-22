"""4. Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.
Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp."""

from sys import *
import os
import shutil
import log



# callback method
def errorHandler(extension_instance):
    print(extension_instance)
    exit()

def writeIntoLogFile():
    fileDescripter = open(logFileName,'w')

    
def printApplicationStatistics(filecopy,filescan):
    log.Logger.writeLog("\n__________Application Statistics___________")
    print(" "*40,"Application Statistics")
    log.Logger.writeLog("Total File Scanned : "+str(filescan))
    print(" "*36,"Total File Scanned : ",filescan)
    log.Logger.writeLog("Total File Copied : "+str(filecopy))
    print(" "*36,"Total File Copied : ",filecopy)
    
def validateExtension(extension):
    return extension.startswith('.') and len(extension)>1

def isExtensionMatched(file,extension):
    return os.path.splitext(file)[1] == extension
    
def copyDirectoryFileToDest(srcdirectory, destdirectory, extension):
    filecopy, filescan = 0,0
    try:
        if os.path.isdir(srcdirectory):
            if validateExtension(extension):
                os.mkdir(destdirectory)
                log.Logger.writeLog("\n_________Copied Files______________")
                for folder, subFolder, filename in os.walk(srcdirectory,onerror = errorHandler):
                    for file in filename:
                        filescan+=1
                        if(not file.startswith('.')):
                            actualpath = os.path.join(folder,file)
                            if isExtensionMatched(actualpath,extension):
                                shutil.copy2(actualpath,destdirectory)
                                log.Logger.writeLog(file)
                                filecopy+=1
                
                printApplicationStatistics(filecopy,filescan)
            else:
                log.Logger.writeLog("Incorrect extension !!!")
                print("Incorrect extension !!!")
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
    print("Directory Traversal Script")
    log.Logger.writeLog("Directory Traversal Script")

    if len(argv) == 2:
        if(argv[1] == '-h' or argv[1] == '-H'):
            print("It's a File copy from source to target directory for specified extension script")
            exit()
    
        if(argv[1] == '-u' or argv[1] == '-U'):
            print("Usage : Provide source, target directory and extension ")
            exit()
    elif len(argv) != 4 or len(argv) == 2:
        print("Error invalid number of arguments")
        exit()
    
    
    
    
    copyDirectoryFileToDest(argv[1], argv[2], argv[3])
    
    log.Logger.closeLogFile()


if __name__ == "__main__":
    main()
