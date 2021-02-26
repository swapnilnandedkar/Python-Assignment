#   2.Write a program which accept N numbers from user and store it into List. Return Maximum
#   number from that List.

#   Input : Number of elements : 7
#   Input Elements : 13 5 45 7 4 56 34
#   Output : 56


import functools

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())
    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
    maxNumber = functools.reduce(lambda no1,no2 : no1 if no1 > no2 else no2,List)
    print("Maximum number in List is : {}".format(maxNumber))

if __name__ == "__main__":
    main()
