#   9. Write a program which accept number from user and return number of digits in that number.
#   Input : 5187934 Output : 7

def Digit(Number):
    
    length = 0
    while(Number > 0):
        length += 1
        Number = int(Number/10)
        
    return length
            
    
def main():
    print("Enter Number")
    Number = int(input())
    
    print("Number {} have {} digit".format(Number,Digit(Number)))
    
if __name__ == "__main__":
    main()

