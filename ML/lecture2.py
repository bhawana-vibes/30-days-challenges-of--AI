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


#for i in range(2, 100 , 2):
 #   print(i)


'''n = int(input("enter the number:"))
sum = 0
for i in range(1 ,n+1):
    sum += i
print(sum)'''

#functions
'''def char():#fun definition
    print("bhawana")
    print("i am a girl")
char()# fun call'''


'''def sum (a ,b):
    s = a+b
    return s
result = sum(123 ,474)
print(result)'''

'''def cal_avg(a ,b ,c):
    sum = a+b+c
    return sum/3
print(cal_avg(3,5,8))


def sum(a ,b=1):
    return a+b
print(sum(10))'''


#factorial N
def cal_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact = fact*i
    return fact
n =int(input("enter the n:"))
print(cal_fact(n))

print("...LECTURE2 DONE....")