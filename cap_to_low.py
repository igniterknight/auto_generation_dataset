x = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
f = len(x)
i = 0
z =[]
while i < f:
    l = x[i].casefold()
    z.append(l)
    i += 1

print(z)