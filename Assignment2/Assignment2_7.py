
def PrintNumberPattern(Number):
    for row in range(1,Number+1):
        for column in range(1,Number+1):
            print(column,end =" ")
        print()
    
def main():
    print("Enter Number")
    Number = int(input())
    
    PrintNumberPattern(Number)
    
if __name__ == "__main__":
    main()

