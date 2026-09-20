'''name = "bhawana hirnwal"
print(len(name))
print(name[5])'''


'''name1 = "bhawana hirnwal"
name2 = "shilpi"

print(name1 +  " " +  name2)'''

'''name = "bhawana hirnwal"
for ch in name:
    print(ch)'''

name = "bhawana"
print(name[1:5])
print(name[0:])
print(name[1:len(name)])
print(name[::])
print(name[-5:-1])

#string formatting
a= 3
b = 5
sum = a+b
#normal formatting
print("sum of {} & {} is {}".format(a, b ,sum))

#index based
print("sum is {2} of {0} & {1}".format(a,b,sum))

#value based
print("values of  vars {a} & {b}".format(a=3 , b=2))