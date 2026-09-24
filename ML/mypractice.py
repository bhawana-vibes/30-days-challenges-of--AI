attempts = 0
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