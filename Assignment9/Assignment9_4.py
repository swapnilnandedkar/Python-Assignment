#   4.Write a program which accept two file names from user and compare contents of both the
#   files. If both the files contains same contents then display success otherwise display failure.
#   Accept names of both the files from command line.

#   Input : Demo.txt Hello.txt
#   Compare contents of Demo.txt and Hello.txt

import os
from sys import argv
    
def openFile(fileName):
    fd = open(fileName,mode = 'r',encoding ='utf-8')
    return fd

def compareFileContent(file1,file2):
    file1Content = file1.read()
    file2Content = file2.read()
    
    return file1Content == file2Content
    
def closeFile(fd):
    fd.close()

        
def main():
    
    if len(argv) == 3:
        if os.path.exists(argv[1]) and os.path.exists(argv[2]):
            file1 = openFile(argv[1])
            file2 = openFile(argv[2])
            
            IsContentMatched = compareFileContent(file1,file2)
            
            if IsContentMatched:
                print("Both file contents are Matched!!!")
            else:
                print("Both file contents doesn't Matched!!!")
            
            closeFile(file1)
            closeFile(file2)
            
        else:
            print("File Not Found!!!!")
    else:
        print("Insufficient Arguments!!!")
 
   
if __name__ == "__main__":
    main()
