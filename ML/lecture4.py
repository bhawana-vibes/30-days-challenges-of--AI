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
print( f"{fru1.name} is price of = {fru1.get_price()}")'''

class student:
    college_name = "abc college"

    def __init__(self , name ,cgpa):
        self.name = name
        self.cgpa = cgpa


stu1 = student("bhawana" , 7.5)
stu2 = student("shilpi" , 8.5)
print(stu1.name)
print(stu2.college_name)