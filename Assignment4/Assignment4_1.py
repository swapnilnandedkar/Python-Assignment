#   1.Write a program which contains one lambda function which accepts one parameter and return
#   power of two.

#   Input : 4 Output : 16
#   Input : 6 Output : 64

import functools

def main():
    
    List = []

    print("Enter number to check its square")
    number = int(input())
    
    
    additionResult = lambda no1 : 2 ** no1 
    print("Addition of numbers in List is : {}".format(additionResult(number)))

if __name__ == "__main__":
    main()
