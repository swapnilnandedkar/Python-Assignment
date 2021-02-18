
def CheckNum(Number):
    isEven = False
    
    isEven = True if (Number % 2 == 0) else False
    return isEven
    

def main():
    print("Enter number to check Even or Odd")
    Number = int(input())
    
    isEven = CheckNum(Number)
    
    if isEven :
        print("Number {} is Even".format(Number))
    else :
        print("Number {} is Odd".format(Number))
    
    
if __name__ == "__main__":
    main()

