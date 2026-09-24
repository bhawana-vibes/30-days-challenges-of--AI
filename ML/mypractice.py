'''attempts = 0
while attempts<3:
    pin = int(input("enter the pin:"))
    if pin == 1234:
        print("granted access")
        break
    else:
        print("wrong pin .try again.")
        attempts += 1
if attempts == 3:
    print ("card blocked")

age = int(input("enter the age:"))
day = input("enter the day:")
if age<12:
    price = 100
elif age<60:
    price = 200
else:
    price = 150
if day =="saturday":
   price = price-50
print("final ticket price:rs.", price)'''

total_amount = int(input("enter the amount:"))
is_member = input("yes/no:")
delivery_charge = 0
if total_amount>= 1000:
    delivery = 0
elif is_member == "yes":
    delivery = 0
else:
    delivery = 50
final = total_amount + delivery
print(final)
print(delivery)