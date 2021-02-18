
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

