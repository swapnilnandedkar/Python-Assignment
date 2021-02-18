
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

