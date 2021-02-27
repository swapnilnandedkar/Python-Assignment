#2. Write a recursive program which display below pattern.
#Input : 5
#Output : 1 2 3 4 5

i = 1
def PrintNumberR(size):
    global i
    if size == 0:
        return
    print(i  ,end=" ")
    i = i + 1
    size =  size - 1
    PrintNumberR(size)

def main():
    
    print("Enter number to print star")
    size = int(input())
    
    PrintNumberR(size)
    print()

if __name__ == "__main__":
    main()
