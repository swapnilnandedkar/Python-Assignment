
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

