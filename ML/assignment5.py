#print("...assignment5 start....")

#que1
'''with open(r"ML\names.txt" , "w") as f:
    for i in range(5):
        name = input(f"enter name {i+1}:")
        f.write(name + "\n")
print("\n adding the names in file.\n")
print("file read names")

with open(r"ML\names.txt" , "r") as f:
    content = f.read()
    print(content)'''

#que2
with open(r"ML\log.txt" , "a") as f:
    f.write("program run successfully\n")
print("all logs in log.txt")

with open(r"ML\log.txt" , "r") as f:
    all_logs = f.read()
    print(all_logs)