#    1.Write a program which accept N numbers from user and store it into List. Return addition of all
#    elements from that List.

#    Input : Number of elements : 6
#    Input Elements : 13 5 45 7 4 56
#    Output : 130

import functools

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())
    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
    additionResult = functools.reduce(lambda no1,no2 : no1 + no2,List)
    print("Addition of numbers in List is : {}".format(additionResult))

if __name__ == "__main__":
    main()
