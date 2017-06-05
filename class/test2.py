f = open("my_vector.py", "r")


print("Case 2: ")
l = f.readlines()
print(l)

f.seek(0)

print("Case 1: ")
ll =  f.read()
print(ll)

f.close()