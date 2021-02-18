
def PrintPattern(Number):
    for row in range(Number):
        for column in range(0,Number-row):
            print("*",end =" ")
        print()
        
        
def main():
    print("Enter Number")
    Number = int(input())
    
    PrintPattern(Number)

if __name__ == "__main__":
    main()

