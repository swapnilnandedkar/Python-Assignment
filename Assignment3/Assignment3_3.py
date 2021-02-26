#   3.Write a program which accept N numbers from user and store it into List. Return Minimum
#   number from that List.

#   Input : Number of elements : 4
#   Input Elements : 13 5 45 7
#   Output : 5


import functools

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())
    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
    minNumber = functools.reduce(lambda no1,no2 : no1 if no1 < no2 else no2,List)
    print("Minimum number in List is : {}".format(minNumber))

if __name__ == "__main__":
    main()
