
def IsNumberDivisibleBy5(Number):
    return True if (Number % 5 == 0) else False
    
def main():
    print("Enter Number to check it's divisible by 5")
    Number = int(input())
    
    result = IsNumberDivisibleBy5(Number)
    
    if result:
        print("Number {} is divisible by 5".format(Number))
    else :
        print("Number {} is not divisible by 5".format(Number))

if __name__ == "__main__":
    main()

