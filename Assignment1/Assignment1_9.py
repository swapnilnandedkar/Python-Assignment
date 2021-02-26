#   9. Write a program which display first 10 even numbers on screen.
#   Output : 2 4 6 8 10 12 14 16 18 20

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

