#   1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#   for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#   parameters as number and perform the operation. Write on python program which call all the
#   functions from Arithmetic module by accepting the parameters from user.

import sys

from Arithmetic import *

def main():
    print("Enter First Number")
    Number1 = int(input())
    
    print("Enter Second Number")
    Number2 = int(input())
    
    print("Addtion of {} and {} is {}".format(Number1,Number2,Addition(Number1,Number2)))
    print("Substraction of {} and {} is {}".format(Number1,Number2,Substraction(Number1,Number2)))
    print("Multiplication of {} and {} is {}".format(Number1,Number2,Multiplication(Number1,Number2)))
    
    if Number2 > 0:
        print("Division of {} and {} is {}".format(Number1,Number2,Division(Number1,Number2)))
    else :
        print("Error: Divide by 0")
    
    
if __name__ == "__main__":
    main()

