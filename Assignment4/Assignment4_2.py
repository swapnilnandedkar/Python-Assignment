#   2.Write a program which contains one lambda function which accepts two parameters and return
#   its multiplication.

#   Input : 4 3 Output : 12
#   Input : 6 3 Output : 18

import functools

def main():
    
    List = []

    print("Enter 1st number for multiplication")
    number1 = int(input())
    
    print("Enter 2nd number for multiplication")
    number2 = int(input())
    
    multiplication = lambda no1,no2 : no1 * no2
    print("Addition of numbers in List is : {}".format(multiplication(number1,number2)))

if __name__ == "__main__":
    main()
