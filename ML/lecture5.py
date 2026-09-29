# file i/o
'''f = open("ML/sample.txt" , "r")
data1 = f.readline()
print(data1)
data = f.read()
print(data)
print(type(data))
f.close()


f = open("ML/sample.txt" , "w")
f.write("bhawana hirnwal is a girl")
f.close()

f = open("ML/sample.txt")
print(f.read())
f.close()


f = open("ML/sample.txt" , "a")
f.write("\nshe is the want to successful a person ")
f.close()

f = open("ML/sample2.txt" , "x")
f.write("python is low level langugae")
f.close()

with open("ML/sample.txt" ,"r") as f:
    data = f.read()
    print(f.read())
    print(len(data))

import os
os.remove("ML/sample2.txt")

#word search

data = True
line = 1
word = "want"

with open("ML/sample.txt" , "r") as f:
    while data:
        data = f.readline()

        if (word in data):
            print(f"{word} found at line {line}")
            break
        print(data)
        line += 1'''

#execption handling
try:
    x = int(input("enter the x:"))
    ans = 10/x

except ZeroDivisionError:
    print(f"divide by 0 not allowed")

else:
    print(f"ans = {ans}")