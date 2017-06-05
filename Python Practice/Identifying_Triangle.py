print("Identifying Triangle Program!")

x = int(input("Write First edge! "))
y = int(input("Write Second edge! "))
z = int(input("Write Third edge! "))

l = [x, y, z]

l.sort()

if (l[2] >= l[0] + l[1]):
    print("Triangles are not created")
elif (l[2] ** 2 == l[0] ** 2 + l[1] ** 2):
    print("This is right triangle")
elif (l[2] ** 2 < l[0] ** 2 + l[1] ** 2):
    print("This is acute triangle")
elif (l[2] ** 2 > l[0] ** 2 + l[1] ** 2):
    print("This is obtuse triangle")
