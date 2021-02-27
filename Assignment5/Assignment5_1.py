#1. Write a recursive program which display below pattern.
#Input : 5
#Output : * * * * *

def PrintStartR(size):
    if size == 0:
        return
    print("* ",end="")
    size =  size - 1
    PrintStartR(size)

def main():
    
    print("Enter number to print star")
    size = int(input())
    
    PrintStartR(size)
    print()

if __name__ == "__main__":
    main()
