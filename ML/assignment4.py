print(".......asignment start.....")

#que1
'''class bankaccount:
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
print("Current Balance:", acc.check_balance())'''

#que2
class book:
    def __init__(self , title , author):
        self.title = title
        self.author = author
        self.reviews = []
    def add_review(self , review):
        self.reviews.append(review)
    def count_reviews(self):
        return len(self.reviews)
    def display_all_reviews(self):
        if not self.reviews:
            print("no reviews yet")
        else:
            print(f"Reviews for '{self.title}':")
            for r in self.reviews:
                print(f"{r}")
b= book("atomic habits" , "james clear")
b.add_review("great book")
b.add_review("must read")


print("total reviews:" , b.count_reviews())
b.display_all_reviews()
