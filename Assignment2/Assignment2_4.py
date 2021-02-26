#   4.Write a program which accept one number form user and return addition of its factors.
#   Input : 12 Output : 16 (1+2+3+4+6)

def FactorAddition(Number):
    sum = 1
    halfNumber = int(Number/2) + 1
    for counter in range(2,halfNumber,1):
        if Number % counter == 0:
            sum += counter
    return sum

def main():
    print("Enter Number")
    Number = int(input())
    
    print("Factor Addition of {} is : {}".format(Number,FactorAddition(Number)))

if __name__ == "__main__":
    main()

