#   8. Write a program which accept number from user and print that number of “*” on screen.
#   Input : 5 Output : * * * * *

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

