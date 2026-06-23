#without encapsulatio
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        self.balance=800
    def show_balance(self):
        print("balance is:",self.balance)
b=BankAccount(30000)
b.show_balance()
b.deposit(20000)
b.show_balance()
print(b.balance)

#with encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def show_balance(self):
        print("balance is:",self.__balance)
b=BankAccount(30000)
b.show_balance()
b.deposit(20000)
b.show_balance()
print(b.__balance)



