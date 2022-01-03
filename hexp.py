from random import randint as r
x = r(150,210)
y = r(160,250)
z = r(180,260)

list = []
i = 0

assign = r(1,3)

if assign == 1:
    #x = r(150,210)
    print("x")
    while i < 50:
        x = r(150,210)
        list.append(x)
        i += 1
elif assign == 2:
    print("y")
    while i < 50:
        y = r(160,250)
        list.append(y)
        i += 1
else:
    print("z")
    while i < 50:
        z = r(180,260)
        list.append(z)
        i += 1

print(list)


    