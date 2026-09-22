#que1
word = input("enter the word:")
if word == word[::-1]:
    print(" yes palindrome:" , word)
else:
    print("not palindrome:" , word)