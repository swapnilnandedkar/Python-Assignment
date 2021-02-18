
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

