#3.Write a recursive program which display below pattern.
#Input : 5
#Output : 5 4 3 2 1


def PrintNumberR(size):
    if size == 0:
        return
    print(size  ,end=" ")
    size =  size - 1
    PrintNumberR(size)

def main():
    
    print("Enter number to print star")
    size = int(input())
    
    PrintNumberR(size)
    print()

if __name__ == "__main__":
    main()
