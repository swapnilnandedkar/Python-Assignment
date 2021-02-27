#4.Write a recursive program which accept number from user and return
#summation of its digits.
#Input : 879
#Output : 24

sum = 0
def SumOfDigitR(number):
    global sum
    if number > 0:
        sum = sum + number % 10
        SumOfDigitR(int(number/10))
    return sum

def main():
    
    print("Enter number")
    number = int(input())
    
    print("Sum of digit {} is : {}".format(number,SumOfDigitR(number)))

if __name__ == "__main__":
    main()
