#   6.Write a program which accept number from user and check whether that number is positive or
#   negative or zero.

#   Input : 11 Output : Positive Number
#   Input : -8 Output : Negative Number
#   Input : 0 Output : Zero

def CheckNumber(Number):
    if Number > 0:
        print("Number {} is Positive".format(Number))
    elif Number < 0:
        print("Number {} is Negative".format(Number))
    else:
        print("Number {} is Zero".format(Number))

def main():
    print("Enter Number")
    Number = int(input())
    
    CheckNumber(Number)

if __name__ == "__main__":
    main()

