#   4.Write a program which accept N numbers from user and store it into List. Accept one another
#   number from user and return frequency of that number from List.

#   Input : Number of elements : 11
#   Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#   Element to search : 5
#   Output : 3



import functools

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())
    
    print("Enter number you want search it's occurance in List")
    number = int(input())

    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
    # Approch 1 with inbuilt count function
    occurance = List.count(number)
    print("Minimum number in List is : {} with count function".format(occurance))
    
    # Approch 2 with filter and then convert it into list and print list length
    occurance = len(list(filter(lambda no1 : no1 == number ,List)))
    print("Minimum number in List is : {} with filter".format(occurance))

if __name__ == "__main__":
    main()
