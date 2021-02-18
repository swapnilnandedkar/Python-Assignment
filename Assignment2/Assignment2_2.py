
def PrintStarPattern(Number):

    for row in range(Number):
        for column in range(Number):
            print("*", end =" ")
        print()
    

def main():
    print("Enter number to print * pattern")
    Number = int(input())
    
    PrintStarPattern(Number)
    
if __name__ == "__main__":
    main()

