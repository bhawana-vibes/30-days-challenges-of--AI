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
print("Current Balance:", acc.check_balance())

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

#que4
class shape:
    def area(self):
        return 0
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*(self.radius**2)
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base * self.height

c = circle(4)
r = rectangle(3,5)
t = triangle(9,7)
print(f"circle : {c.area()}")
print(f"rectangle : {r.area()}")
print(f"triangle : {t.area()}")

#que6
from abc import ABC, abstractmethod


class Employee(ABC):

  def __init__(self, name):
    self.name = name

  @abstractmethod
  def cal_salary(self):
    pass


class Intern(Employee):

  def __init__(self, name, hours_worked, hourly_rate):
    super().__init__(name)
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate

  def cal_salary(self):
    return self.hours_worked * self.hourly_rate


class FullTime(Employee):

  def __init__(self, name, monthly_salary): 
    super().__init__(name)  
    self.monthly_salary = monthly_salary  

  def cal_salary(self):
    return self.monthly_salary


ft = FullTime("Piyush", 50000)
it = Intern("Aman", 100, 50)

print(f"{ft.name} salary: Rs {ft.cal_salary()}")
print(f"{it.name} salary: Rs {it.cal_salary()}")

#que7
class person:
    def __init__(self , name , age=None , address=None):
        self.name = name
        self.age = age 
        self.address = address

    def display_info(self):
        print(f"name:{self.name} , age:{self.age} , address:{self.address}")

p1 = person("bhawana")
p2 = person("priya" , 21)
p3 = person("shilpi" , 22 ,"delhi")


p1.display_info()
p2.display_info()
p3.display_info()'''

#que8
class player:
    player_count = 0
    def __init__(self, name , level):
        self.name = name
        self.level = level
        player.player_count += 1

    def display(self):
        print(f"player: {self.name} , level:{self.level}")
p1 = player("alice" , 1)
p2 = player("bob" , 5)
p3 = player("charlie" , 11)

p1.display()
p2.display()
p3.display()

print(f"total players: {player.player_count}")







