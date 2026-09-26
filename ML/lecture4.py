#print("lecture4 start")

'''class student:
    name = "bhawana"
    college = "abc"
    year = "4th"
stu1 = student()
stu2 = student()
l = [1,2]
print(type(l))
print(type(stu1))
print(type(stu2))
#print(stu1.name , stu1.year , stu1.college)
#print(stu2.name , stu2.year , stu2.college)


class frutis:
    def __init__(self):
        print("this is calling contructor")
fru1 = frutis()
fru2 = frutis()


class frutis:
    def __init__(self , name, price):parameterized 
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
fru1 = frutis("apple" , 50)
fru2 = frutis("mango" , 40)

print(fru1.name)
print(fru2.name)

print(fru1.get_price())
print( f"{fru1.name} is price of = {fru1.get_price()}")

class student:
    college_name = "abc college"

    def __init__(self , name ,cgpa):
        self.name = name
        self.cgpa = cgpa


stu1 = student("bhawana" , 7.5)
stu2 = student("shilpi" , 8.5)
print(stu1.name)
print(stu2.college_name)


class laptop:
    storage_type = "ssd"

    def __init__(self , RAM ,storage):
        self.RAM = RAM
        self.storage = storage
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):#instance method
        print(f"laptp has {self.RAM} RAM & {self.storage} {self.storage_type}")
l1 = laptop("16gb","512gb")
#l2 = laptop("8gb","256gb")
#l1.get_info()

print(laptop.get_storage_type())'''


class Product:
    count = 0
    def __init__(self , name , price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"price of {self.name} is rs . {self.price}")
    @classmethod
    def get_count(cls):
        print(f"total product is , {cls.count}")

p1 = Product("laptop" , 50000)
p2 = Product("phone" , 10000)
p3 = Product("pen" , 5)

#p1.get_info()
Product.get_count()