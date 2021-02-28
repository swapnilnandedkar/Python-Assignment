#   1.Write a program which contains one class named as Demo.
#   Demo class contains two instance variables as no1 ,no2.
#   That class contains one class variable as Value.
#   There are two instance methods of class as Fun and Gun which displays values of instance
#   variables.
#   Initialise instance variable in init method by accepting the values from user.
#   After creating the class create the two objects of Demo class as

#   Obj1 = Demo(11,21)
#   Obj2 = Demo(51,101)
#   Now call the instance methods as
#   Obj1.Fun()
#   Obj2.Fun()
#   Obj1.Gun()
#   Obj2.Gun()

class Demo:
    value = 11
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
        
    def Fun(self):
        print("inside fun with value {} and {}".format(self.no1,self.no2))
        
    def Gun(self):
        print("inside gun with value {} and {}".format(self.no1,self.no2))
        
def main():
    
    print("Class variable value is : ",Demo.value)
    print("Enter number1")
    number1 = int(input())
    
    print("Enter number2")
    number2 = int(input())
    
    Obj1 = Demo(number1,number2)
    Obj1.Fun()
    Obj1.Gun()
    print("Enter number1")
    number1 = int(input())
    
    print("Enter number2")
    number2 = int(input())
    Obj2 = Demo(number1,number2)
    Obj2.Fun()
    Obj2.Gun()
   
if __name__ == "__main__":
    main()
