import random
n = (int(input("Write Number of Phone you Need: ")))
y = [random.randint(6000000000,9999999999)]
i = 0

while i < (n - 1):
    l = random.randint(6000000000,9999999999)
    if l in y:
        continue
    else:
        y.append(l)
        i += 1

print(y)