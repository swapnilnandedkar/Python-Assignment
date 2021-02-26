#   5.Write a program which accept N numbers from user and store it into List. Return addition of all
#   prime numbers from that List. Main python file accepts N numbers from user and pass each
#   number to ChkPrime() function which is part of our user defined module named as
#   MarvellousNum. Name of the function from main python file should be ListPrime().

#   Input : Number of elements : 11
#   Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#   Output : 32 (13 + 5 + 7 +2 + 5)



from MarvellousNum import *


def ListPrime(list):
    sum = 0
    for icnt in range(len(list)):
        if CheckPrime(list[icnt]) == True:
            sum += list[icnt]
    return sum
        

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())

    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
   
    primeSum = ListPrime(List)
    print("Prime number sum in List is : {}".format(primeSum))
    
if __name__ == "__main__":
    main()
