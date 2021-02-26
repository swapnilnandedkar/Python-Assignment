#   3.Write a program which contains filter(), map() and reduce() in it. Python application which
#   contains one list of numbers. List contains the numbers which are accepted from user. Filter
#   should filter out all such numbers which greater than or equal to 70 and less than or equal to
#   90. Map function will increase each number by 10. Reduce will return product of all that
#   numbers.

#   Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#   List after filter = [76, 89, 86, 90, 70]
#   List after map = [86, 99, 96, 100, 80]
#   Output of reduce = 6538752000


import functools

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())
    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
    # Number greater than or equal to 70 and less than or equal to 90
    newdata1 = list(filter(lambda no1 : no1 >= 70 and no1 <= 90,List))
    print("Result of filter is : {}".format(newdata1))
    
    # Increase number by 10 from newdata1
    newdata2 = list(map(lambda no1 : no1 + 10,newdata1))
    print("Result of map is : {}".format(newdata2))
    
    # product of all numbers in newdata2
    newdata3 = functools.reduce(lambda no1,no2 : no1 * no2,newdata2)
    print("Result of reduce is : {}".format(newdata3))

if __name__ == "__main__":
    main()
