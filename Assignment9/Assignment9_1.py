#   1.Write a program which accepts file name from user and check whether that file exists in
#   current directory or not.
#
#   Input : Demo.txt
#   Check whether Demo.txt exists or not.

import os

def FileExists(fileName):
    fileDescripter = None
    try:
        fileDescripter = open(fileName,mode ='r',encoding='utf-8')
    except FileNotFoundError as e:
        print("Exception : ",e)
        return False
    
    fileDescripter.close()
    return True

def FileExistsWithExistingFunction(fileName):
    return os.path.exists(fileName)
    
        
def main():

    print("Enter file name to check it exists :")
    fileName = input()
    
    fileDescripter = FileExists(fileName)
    
    if fileDescripter:
        print("File {} is exists!!! Checked with open method".format(fileName))
    else:
        print("File {} not found!!! Checked with open method".format(fileName))
        
    if FileExistsWithExistingFunction(fileName):
        print("File {} is exists!!! Checked with os module".format(fileName))
    else:
        print("File {} not found!!! Checked with os module".format(fileName))
        
if __name__ == "__main__":
    main()
