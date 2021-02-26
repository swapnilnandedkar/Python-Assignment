#   5.Write a program which display 10 to 1 on screen.
#   Output : 10 9 8 7 6 5 4 3 2 1


def DisplayReverseNumber(StartNumber,EndNumber):
    while EndNumber >= StartNumber :
        print(EndNumber,end =" ")
        EndNumber = EndNumber - 1

def main():
    print("Enter Start number")
    Start = int(input())
    
    print("Enter End number")
    End = int(input())
    
    if Start < End :
        DisplayReverseNumber(Start,End)
    else :
        print("Error : Start should be less than End")
    
    print()   

if __name__ == "__main__":
    main()

