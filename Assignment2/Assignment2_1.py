#from Arithmetic import *
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

