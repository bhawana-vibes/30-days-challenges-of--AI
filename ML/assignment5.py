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
    print(content)

#que2
with open(r"ML\log.txt" , "a") as f:
    f.write("program run successfully\n")
print("all logs in log.txt")

with open(r"ML\log.txt" , "r") as f:
    all_logs = f.read()
    print(all_logs)

#que3
list = [5,10,15,20,25]
new_list = [x for x in list if x>15]
print("original list" , list)
print("new_list" , new_list)

#que4
import json
cities_data = {
    "delhi" : 30000,
    "mumbai" : 50000,
    "bengaluru" : 1300000
}
with open(r"ML\cities.json" , "w") as f:
    json.dump(cities_data , f , indent=4)

with open(r"ML\cities.json" , "r") as f:
    loaded_data = json.load(f)
for city,population in loaded_data.items():
    print(city, ":" , population)

city = input("enter city name:")
population = int(input("enter population:"))

cities_data[city] = population

with open(r"ML\cities.json" , "w") as f:
    json.dump(cities_data , f , indent=4)
print("city added successfully")'''

#que5

try:
    with open("data.txt" , "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("file not found")
