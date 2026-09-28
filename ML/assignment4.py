# file i/o
f = open("ML/sample.txt" , "r")
data = f.readline()
print(data)
print(type(data))
f.close()