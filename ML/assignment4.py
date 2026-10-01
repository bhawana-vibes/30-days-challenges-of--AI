print(".......asignment start.....")

#que1
class bankaccount:
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self , amount):
        self.balance = self.balance+amount
    def withdraw(self, amount):
        if(amount>self.balance):
            print("Insufficient funds")
        else:
            self.balance = self.balance-amount
    def check_balance(self):
        return self.balance

acc = bankaccount("101", "Piyush", 500)
acc.deposit(200)
acc.withdraw(100)
print("Current Balance:", acc.check_balance())
