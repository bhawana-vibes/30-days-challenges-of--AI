#conditional
'''age = int(input("enter the age:"))
if age>18:
    print("you can vote")
else:
    print("you cann't vote")'''

'''age = int(input("enter the age:"))
if age>21:
    print("you can  use phone")
else:
    print("you cann't use phone")'''


'''color = input("enter the color:")
if color =="red":
    print("stop")
elif color =="yellow":
    print("look")
elif color =="green":
    print("go")
else:
    print("wrong color in traffic rules")'''


'''age = int(input("enter the age:"))
if age<13:
    print("child")
elif age<18:
    print("teenager")
else:
    print("adult")'''

'''username = input("enter the name:")
password = input("enter the password:")
if (username=="admin" and password=="pass"):
    print("....LOGIN DONE....")
elif (username != "admin"):
    print("wrong username")
else:
    print("wrong password")'''

'''n = int(input("enter the number:"))
if (n%18==0):
    print("multiple of 18")
else:
    print("not multiple of 18")'''

'''n = int(input("enter the number:"))
if (n%2 == 0):
    print("even number")
else:
    print("odd number")'''

#loops
'''i = 1
while(i <= 10):
    print("bhawana" , i )
    i= i+1

i = 5
while(i >= 1):
    print(i)
    i=i-1

n = int(input("enter the number:"))
i = 1
while(i <= 10):
    print(n*i)
    i = i+1'''

string = "bhawana"
for var in string:
    print(var)


word = "artificial intelligence"
count = 0
for ch in word:
    if (ch =='i'):
        count += 1
print("count of i =" , count)


word = "bhawana"
count = 0
for ch in word:
    if (ch == 'a'):
        count += 1
print("count of vowels =" , count)


#loops in range
#for i in range(10):
    #print(i)

#for i in range(1 , 11):
   # print(i)


for i in range(2, 100 , 2):
    print(i)