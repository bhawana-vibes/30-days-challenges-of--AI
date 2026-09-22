'''name = "bhawana hirnwal"
print(len(name))
print(name[5])'''


'''name1 = "bhawana hirnwal"
name2 = "shilpi"

print(name1 +  " " +  name2)'''

'''name = "bhawana hirnwal"
for ch in name:
    print(ch)'''

'''name = "bhawana"
print(name[1:5])
print(name[0:])
print(name[1:len(name)])
print(name[::])
print(name[-5:-1])'''

#string formatting
'''a= 3
b = 5
sum = a+b
#normal formatting
print("sum of {} & {} is {}".format(a, b ,sum))

#index based
print("sum is {2} of {0} & {1}".format(a,b,sum))

#value based
print("values of  vars {a} & {b}".format(a=3 , b=2))

#f-string
a = 5
b = 7
print(f"sum of {a} & {b} is {a+b}")
print(f"avg of {a} & {b} is {(a+b)/2}")'''

#lists
marks = [57,67,98,76,90]
'''marks[2] = 88
print(len(marks))
print(marks)
print(type(marks))
print(marks[0:5])
marks.append(99)
marks.insert(3 , 70)
marks.sort()
marks.reverse()
print(marks)

#using for loop with lists
#marks = [57,67,98,76,90]
#for val in marks:
   # print(val)
#linear search
marks = [57,67,98,76,90]
x = 98
idx = 0
for val in marks:
  if val == x:
    print(idx)
    break 
  idx = idx +1'''

#tuple
'''digits = (1,2,3, 4,5,6)
print(digits)
print(type(digits))
print(digits[3])
#digits[2] =45 #not allow this line
print(digits[0:2])'''

'''digits = (1,2,3,4,5,6)
for val in digits:
    print(val)

sum = 0
for val in digits:
    sum += val
print(sum)

num = (2,4,6,8,6,9,4)
print(num.index(4))
print(num.count(6))'''

#dictionary
'''info = {
    "name" : "bhawana hirnwal",
    "city" : "bijnor",
    "cgpa" : 85,
    "professional" : "tech"
}
info["cgpa"] = 7.52
print(info)
print(type(info))
print(info["professional"])'''

#dictionary methods
'''info = {
    "name" : "bhawana hirnwal",
    "city" : "bijnor",
    "cgpa" : 85,
    "professional" : "tech"
}
print(info.keys())
print(info.values())
print(info.items())
print(info.get("cgpa"))'''

#sets
'''s = {1,2 ,3 ,3  , 4, 5 , 5,}
s.add(6)
print(len(s))
print(s)
print(type(s))
empty_set = set()
print(empty_set)

#sets methods
s = {1,2 ,3 ,3  , 4, 5 , 5,}
#s.clear()
print(s)
s.pop()
print(s)'''

#student enrolments
info = [
    ("alice" , "math"),
    ("bob" , "science"),
    ("alice" , "science"),
    ("charlie" , "math"),
    ("bob" ,"math"),
    ("alice" , "english"),
    ("charlie" , "english")
]
#course_set = set()
#for tup in info:
 #   course_set.add(tup[1])
#print(course_set)

#for name , course in info:
    #if(course == "english"):
       # print(name)

'''dict = {}
for name , course in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
         dict[name].add(course)
print(dict)'''

print("......lecture3 done......")