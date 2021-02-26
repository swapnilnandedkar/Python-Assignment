#   4.Write a program which display 5 times Marvellous on screen.
#   Output : Marvellous
#   Marvellous
#   Marvellous
#   Marvellous
#   Marvellous

def PrintNTimes(Number):
    for counter in range(Number):
        print("Marvellous")

def main():
    print("Enter Number to iterate string")
    Number = int(input())
    PrintNTimes(Number)

if __name__ == "__main__":
    main()

