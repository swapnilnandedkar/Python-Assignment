#   4.Write a program which contains filter(), map() and reduce() in it. Python application which
#   contains one list of numbers. List contains the numbers which are accepted from user. Filter
#   should filter out all such numbers which are even. Map function will calculate its square.
#   Reduce will return addition of all that numbers.

#   Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#   List after filter = [2, 4, 4, 2, 8, 10]
#   List after map = [4, 16, 16, 4, 64, 100]

#   Output of reduce = 204



import functools

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())
    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
    # filter out all such numbers which are even
    newdata1 = list(filter(lambda no1 : no1 % 2 == 0,List))
    print("Result of filter is : {}".format(newdata1))
    
    # Map function will calculate its square
    newdata2 = list(map(lambda no1 : no1 ** 2,newdata1))
    print("Result of map is : {}".format(newdata2))
    
    # Reduce will return addition of all that numbers.
    newdata3 = functools.reduce(lambda no1,no2 : no1 + no2,newdata2)
    print("Result of reduce is : {}".format(newdata3))

if __name__ == "__main__":
    main()
