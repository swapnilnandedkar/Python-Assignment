#   10. Write a program which accept number from user and return addition of digits in that number.
#   Input : 5187934 Output : 37

def AdditionOfDigit(Number):
    
    sum = 0
    while(Number > 0):
        sum += (Number%10)
        Number = int(Number/10)
        
    return sum
            
    
def main():
    print("Enter Number")
    Number = int(input())
    
    print("Addition of digit's is {} for {} number".format(AdditionOfDigit(Number),Number))
    
if __name__ == "__main__":
    main()

