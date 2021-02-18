
def DisplayEvenRange(Number):
    
    for counter in range(Number):
        print((counter+1)*2,end=" ")
    
def main():
    print("Enter Number to print Even Number range")
    Number = int(input())
    
    DisplayEvenRange(Number)
    print()
    
if __name__ == "__main__":
    main()

