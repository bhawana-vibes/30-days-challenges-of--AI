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
fru2 = frutis()'''


class frutis:
    def __init__(self , name):
        self.name = name
fru1 = frutis("apple")
fru2 = frutis("mango")

print(fru1.name)
print(fru2.name)