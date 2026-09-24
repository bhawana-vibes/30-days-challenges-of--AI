#que1
'''salary = float(input("enter the salary:"))
if (salary<300000):
    tax = "5%"
elif (salary<700000):
    tax = "15%"
else:
    tax = "25%" 
print("tax rate:" , tax)'''

#que2
'''def  print_even(a,b):
    for num in range(a , b+1):
        if (num%2 == 0):
            print(num)

num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))
            
print_even(num1 , num2)

#step 2 without input given
def  print_even(a,b):
    for num in range(a , b+1):
        if (num%2 == 0):
            print(num)
            
print_even(1,50)'''

#que3
'''def print_digits(n):
    while n>0:
       digit = n%10
       print(digit)
       n = n//10
print_digits(456)

#que4
def count_digits(n):
    count = 0
    while n>0:
       n= n//10
       count = count+1
    return count
n = int(input("enter the number:"))  
print(count_digits(n))

#que5
def sum_digits(n):
    sum = 0
    while n>0:
       digits= n % 10
       sum = digits+sum
       n= n//10
    return sum
n = int(input("enter the number:"))  
print(sum_digits(n))'''

#que6

'''#n = int(input("enter the number:"))
for n in range(1 , 101):
 if (n%3==0 and n%5 == 0):
    print("multiple of 3 or 5:" , n)'''


#que7
'''while True:
  n = input("enter the number:")
  if n == "quit":
    print("program stop")
    break
  num = float(n)

  if num>0:
    print("positive")
  elif num<0:
    print("negative")
  else:
    print("zero")'''

#que8
def calculator(a , b , operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    else:
        return "invalid operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
result = calculator(num1, num2, op)
print("Result:", result)

#que9
'''def prime_num(n):
    if n < 2:
        return False
    for i in range(2 , n):
        if n % i ==0:
            return False
    return True
num = int(input("Enter a number: "))
print(prime_num(num))'''


#que10
'''secert_number = 25
while True:
    guess = int(input("enter the number:"))
    if guess > secert_number:
        print("too high")
    elif guess < secert_number:
        print("too low")
    else:
        print("correct!")
        break


print("......ASSINGMENT2 DONE.......")'''



    
