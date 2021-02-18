
def IsPrime(Number):

    isNumberPrime = True
    if Number == 2:
        isNumberPrime = True
    elif Number < 1 or Number%2 == 0:
        isNumberPrime = False
    else:
        counter = 3
        while(counter*counter <= Number):
            if(Number%counter == 0):
                isNumberPrime = False
                break
            counter+=1
        
    return isNumberPrime
        

    
    return isNumberPrime

def main():
    print("Enter number")
    Number = int(input())
    
    if IsPrime(Number):
        print("Number {} is Prime".format(Number))
    else:
        print("Number {} is not Prime".format(Number))

if __name__ == "__main__":
    main()

