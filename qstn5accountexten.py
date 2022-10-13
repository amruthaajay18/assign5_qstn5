class Account:

    def __init__(self,title=None,balance=0):
         self.title=title
         self.balance=balance
    def getbalance(self):
       self.balance=2000

    def deposit(self,amount):
        addedtotal=amount+self.balance
        return addedtotal
    def withdrawal(self,amount):
        subtotal=self.balance-amount
        return subtotal
                

class SavingsAccount(Account):

    def __init__(self,title=None,balance=0,interestrate=0):
        super().__init__(title, balance)
        self.interestRate = interestrate
    def interestammount(self):
        #self.intersetRate=5
        interestammou1=((self.interestRate*self.balance)/100)
        return interestammou1
obj2=SavingsAccount("Ashish",2000,5)
obj2.getbalance()
print(obj2.deposit(500))
print(obj2.withdrawal(500))
print(obj2.interestammount())