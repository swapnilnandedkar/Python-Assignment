#   3. Write a program which accept one number from user and return its factorial.
#   Input : 5 Output : 120

def Factorial(Number):
    sum = 1
    for counter in range(Number):
        sum = sum * (counter +1)
    return sum

def main():
    print("Enter Number to check it's factorial")
    Number = int(input())
    
    print("Factorial of {} is : {}".format(Number,Factorial(Number)))

if __name__ == "__main__":
    main()

