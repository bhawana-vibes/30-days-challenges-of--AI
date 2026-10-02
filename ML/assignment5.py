#print("...assignment5 start....")

#que1
with open("ML\names.txt" , "w") as f:
    for i in range(5):
        name = input(f"enter name {i+1}:")
        file.write(name + "\n")
print("\n adding the names in file.\n")
print("file read names")

with open("ML\names.txt" , "a") as f:
    content = file.read()
    print(content)