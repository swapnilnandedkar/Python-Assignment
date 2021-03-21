#   3.Write a program which accept file name from user and create new file named as Demo.txt and
#   copy all contents from existing file into new file. Accept file name through command line
#   arguments.

#   Input : ABC.txt
#   Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

import os

def openFile(fileName,fileOpenMode):
    fd = open(fileName,mode = fileOpenMode,encoding ='utf-8')
    return fd

def closeFile(fd):
    fd.close()

def copyFile(fdRead,fdWrite):
    for line in fdRead:
        fdWrite.write(line)
    
       
def main():
    print("Enter file name to copy data into new file :")
    fileName = input()
    
    if os.path.exists(fileName):
        fdRead = openFile(fileName,'r')
        fdWrite = openFile("Demo.txt",'w')
        copyFile(fdRead,fdWrite)
        fdRead.close()
        fdWrite.close()
        print("File copied Successfully!!!")
    else:
        print("File {} not found!!!".format(fileName))
   
if __name__ == "__main__":
    main()
