#    3. Write a program which contains one class named as Arithmetic.
#    Arithmetic class contains two instance variables as Value1 ,Value2.
#    Inside init method initialise all instance variables to 0.
#    There are three instance methods inside class as Accept(), Addition(), Subtraction(),
#    Multiplication(), Division().
#    Accept method will accept value of Value1 and Value2 from user.
#    Addition() method will perform addition of Value1 ,Value2 and return result.
#    Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
#    Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
#    Division() method will perform division of Value1 ,Value2 and return result.
#    After designing the above class call all instance methods by creating multiple objects.


class Arithmetic:
    PI = 3.14
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
         
    def Accept(self):
        print("Enter value1")
        self.Value1 = int(input())
        
        print("Enter value2")
        self.Value2 = int(input())
    
    def Addition(self):
        return self.Value1 + self.Value2
        
    def Subtraction(self):
        return self.Value1 - self.Value2
        
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            print("Error : Divide by zero")
        else:
            return self.Value1 / self.Value2
    
def main():
    
    Obj1 = Arithmetic()
    Obj1.Accept()
    print("Addition of {} and {} is : {}".format(Obj1.Value1,Obj1.Value2,Obj1.Addition()))
    print("Substraction of {} and {} is : {}".format(Obj1.Value1,Obj1.Value2,Obj1.Subtraction()))
    print("Multiplication of {} and {} is : {}".format(Obj1.Value1,Obj1.Value2,Obj1.Multiplication()))
    print("Division of {} and {} is : {}".format(Obj1.Value1,Obj1.Value2,Obj1.Division()))
    
    Obj2 = Arithmetic()
    Obj2.Accept()
    print("Addition of {} and {} is : {}".format(Obj2.Value1,Obj2.Value2,Obj2.Addition()))
    print("Substraction of {} and {} is : {}".format(Obj2.Value1,Obj2.Value2,Obj2.Subtraction()))
    print("Multiplication of {} and {} is : {}".format(Obj2.Value1,Obj2.Value2,Obj2.Multiplication()))
    print("Division of {} and {} is : {}".format(Obj2.Value1,Obj2.Value2,Obj2.Division()))
   
if __name__ == "__main__":
    main()
