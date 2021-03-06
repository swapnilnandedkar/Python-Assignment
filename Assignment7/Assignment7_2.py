#    2. Write a program which contains one class named as BankAccount.
#    BankAccount class contains two instance variables as Name & Amount.
#    That class contains one class variable as ROI which is initialise to 10.5.
#    Inside init method initialise all name and amount variables by accepting the values from user.
#    There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
#    CalculateIntrest().
#    Deposit() method will accept the amount from user and add that value in class instance variable
#    Amount.
#    Withdraw() method will accept amount to be withdrawn from user and subtract that amount
#    from class instance variable Amount.
#    CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
#    which is Class variable as ROI.
#    And Display() method will display value of all the instance variables as Name and Amount.
#    After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5
    def __init__(self,Name):
        self.Name = Name
        self.Amount = 0
        
    def Display(self):
        print("Customer Name : ",self.Name)
        print("Customer Amount : ",self.Amount)
    
    def Deposit(self,Amount):
        self.Amount += Amount
    
    def Withdraw(self,Amount):
        if(Amount > self.Amount):
            print("Error: you do not have sufficient balance")
            return
        self.Amount -= Amount
    
    def CalculateIntrest(self):
        Interest = (self.Amount * BankAccount.ROI * 1)/100                      # Interest for 1 year
        print("Interest on amount {} is : {}".format(self.Amount,Interest))
        
        
def main():
    
    print("Enter Customer Name : ")
    CustomerName = input()
    
    Obj1 = BankAccount(CustomerName)
    print("Enter Amount to Deposit")
    DepositAmount = int(input())
    
    Obj1.Deposit(DepositAmount)
    Obj1.CalculateIntrest()
    Obj1.Display()
    
    print("Enter Amount to Withdraw")
    WithdrawAmount = int(input())
    Obj1.Withdraw(WithdrawAmount)
    Obj1.CalculateIntrest()
    Obj1.Display()
    
    print("Enter Customer Name : ")
    CustomerName = input()
    
    Obj2 = BankAccount(CustomerName)
    print("Enter Amount to Deposit")
    DepositAmount = int(input())
    
    Obj2.Deposit(DepositAmount)
    Obj2.CalculateIntrest()
    Obj2.Display()
    
    print("Enter Amount to Withdraw")
    WithdrawAmount = int(input())
    Obj2.Withdraw(WithdrawAmount)
    Obj2.CalculateIntrest()
    Obj2.Display()
    

   
if __name__ == "__main__":
    main()
