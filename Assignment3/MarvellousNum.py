
def CheckPrime(Number):

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
    

