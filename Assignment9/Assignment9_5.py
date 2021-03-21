#   5. Accept file name and one string from user and return the frequency of that string from file.

#   Input : Demo.txt Marvellous
#   Search “Marvellous” in Demo.txt
#   Approch 1 : use manual counter
#   Approch 2 : use collection counter

import os
import sys
import collections

    
def openFile(fileName):
    fd = open(fileName,mode = 'r',encoding ='utf-8')
    return fd

def GetCountManual(fd,searchString):
    count = 0
    wordList = fd.read().split()
    for icnt in range(len(wordList)):
        if wordList[icnt] == searchString:
            count = count + 1
    return count

def GetCountByCollections(fd,searchString):
    fd.seek(0)
    collection = collections.Counter(fd.read().split())
    return collection[searchString]

def closeFile(fd):
    fd.close()

        
def main():
    print("Enter File name in which you want to search string frqeuncy: ")
    fileName = input();
    
    print("Enter String : ")
    searchString = input()
    
    if os.path.exists(fileName):
        fd = openFile(fileName)
        manualCount = GetCountManual(fd,searchString)
        print("word {} found in file {} times using manual counter.".format(searchString,manualCount))
        
        collectionCount = GetCountByCollections(fd,searchString)
        print("word {} found in file {} times using collection counter.".format(searchString,collectionCount))
        
        closeFile(fd)
    else:
        print("File Not Found!!!!")
 
   
if __name__ == "__main__":
    main()
