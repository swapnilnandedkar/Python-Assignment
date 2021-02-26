#   5.Write a program which contains filter(), map() and reduce() in it. Python application which
#   contains one list of numbers. List contains the numbers which are accepted from user. Filter
#   should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
#   return Maximum number from that numbers. (You can also use normal functions instead of
#   lambda functions).

#   Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#   List after filter = [2, 11, 17, 23, 31]
#   List after map = [4, 22, 34, 46, 62]

#   Output of reduce = 62

import functools

def CheckPrime(Number):

    isNumberPrime = True
    if Number == 2:
        isNumberPrime = True
    elif Number < 1 or Number%2 == 0:
        isNumberPrime = False
    else:
        counter = 3
        while(counter*counter <= Number):
            if(Number%counter == 0):
                isNumberPrime = False
                break
            counter+=1
        
    return isNumberPrime

def main():
    
    List = []

    print("Enter total number you want to insert in List")
    listSize = int(input())
    
    for icnt in range(listSize):
        print("Enter {} number".format(icnt+1))
        List.append(int(input()))
    
    # filter out all such numbers which are prime
    newdata1 = list(filter(CheckPrime,List))
    print("Result of filter is : {}".format(newdata1))
    
    # Map function will multiply number by 2
    newdata2 = list(map(lambda no1 : no1 * 2,newdata1))
    print("Result of map is : {}".format(newdata2))
    
    # Reduce will return max number
    newdata3 = functools.reduce(lambda no1,no2 : no1 if no1 > no2 else no2,newdata2)
    print("Result of reduce is : {}".format(newdata3))
    
if __name__ == "__main__":
    main()
