#   2. Write a program which accept file name from user and open that file and display the contents
#   of that file on screen or write.

#   Input : Demo.txt , ask want to update file type Y or N
#   Display contents of Demo.txt on console.

import os

class File:
    def __init__(self,fileName):
        self.fileName = fileName
        self.fd = None
    
    def isFileExists(self):
        return os.path.exists(self.fileName)
        
    def openFile(self,openMode):
        try:
            self.fd = open(self.fileName,mode = openMode,encoding ='utf-8')
            return True
        except PermissionError:
            print("Not allowed to update File!!! But you can read data!!!")
            self.fd = open(self.fileName,mode = 'r',encoding ='utf-8')
            return False
        
    def readFile(self):
         if self.fd != None:
            self.fd.seek(0)
            print("Read : ",self.fd.read())
    
    def writeFile(self,data):
        if self.fd != None:
            self.fd.write(data)

    def closeFile(self):
        if self.fd != None:
            self.fd.close()
            print("file closed successfully!!!")

        
def main():
    print("Enter file name to read data from it :")
    fileName = input()

    fobj = File(fileName)
    if fobj.isFileExists():
        print("Enter Y for update file N for no")
        
        updateFile = input().strip()
        if updateFile == 'Y' or updateFile == 'y':
            
                if fobj.openFile('a+'):
                    print("Enter Data you want to insert in file :")
                    data = input()
                    fobj.writeFile("\n"+data)
        else:
            fobj.openFile('r')
    else:
        print("File Not Found!!!!")
    
    fobj.readFile()
    fobj.closeFile()
   
if __name__ == "__main__":
    main()
