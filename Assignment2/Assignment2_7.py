#   7. Write a program which accept one number and display below pattern.

#   Input : 3
#   Output : 1 2 3 4 5
#            1 2 3 4 5
#            1 2 3 4 5

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

