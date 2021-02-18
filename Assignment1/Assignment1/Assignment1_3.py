
def Addition( Number1 , Number2 ):
    return Number1 + Number2

def main():
    print("Enter 1st Number for addition")
    Number1 = int(input())
    
    print("Enter 2nd Number for addition")
    Number2 = int(input())
    
    print("Addition of {} and {} is : {}".format(Number1,Number2, Addition(Number1,Number2)))

if __name__ == "__main__":
    main()

