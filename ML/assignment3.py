#que1
'''word = input("enter the word:")
if word == word[::-1]:
    print(" yes palindrome:" , word)
else:
    print("not palindrome:" , word)'''

#que2
'''number = [10,30,40,45,56,60]
avg = sum(number) / len(number)
print(avg)'''

#que3
'''#list1 = list[int(input("enter the numbers:"))]
#list2 = list[int(input("enter the numbers:"))]
list1 = [1,2,7]
list2 = [2,4,5]
merge_list = list1+list2
merge_list.sort()
print(merge_list)'''

#que4
'''tup = (2,4,6,7,8,9,11,23,15,18)
even_list = []
odd_list = []
for num in tup:
    if num % 2 ==0:
        even_list.append(num)
    else:
        odd_list.append(num)
even_tuple = tuple(even_list)
odd_tuple = tuple(odd_list)
print(even_tuple)
print(odd_tuple)'''

'''#que6
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict = {}
for w in words:
    dict[w] = len(w)
print(dict)'''

#que7
'''text = input("enter the text:")
spaces = text.count(" ")
print(spaces)'''

#que8
'''list1 = [1,2,3,4]
list2 = [5,6,7,8]
common = set(list1) & set(list2)
if len(common) == 0:
    print("no common number")
else:
    print("yes common number" , common)'''

#que9
'''numbers = [1, 2, 3, 2, 4, 5, 1, 6, 2]
seen = set()
duplicates = set()
for items in numbers:
    if items in seen:
        duplicates.add(items)
    else:
        seen.add(items)
print(list(duplicates))
print(list(seen))'''

#que10
'''text = input("enter the text:")
unique = set(text)
print(unique)
print(len(unique))'''


print(".....assignment3 done......")


