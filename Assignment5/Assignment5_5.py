#5. Write a recursive program which accept number from user and return its
#factorial.
#Input : 5
#Output : 120

factorial = 1
def FactorialR(number):
    global factorial
    if number > 0:
        factorial = factorial * number
        FactorialR(number-1)
    return factorial

def main():
    
    print("Enter number")
    number = int(input())
    
    print("factorial of digit {} is : {}".format(number,FactorialR(number)))

if __name__ == "__main__":
    main()
