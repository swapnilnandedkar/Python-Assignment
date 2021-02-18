
def DisplayStarPattern(Number):
    
    for counter in range(Number):
        print("*", end=" ")
    
def main():
    print("Enter Number to print * pattern")
    Number = int(input())
    
    DisplayStarPattern(Number)
    print()
    
if __name__ == "__main__":
    main()

