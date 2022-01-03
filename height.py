from random import uniform as u
from age import age
from gender import gender

#Age starts from 21 and above


x =[]
i = 0
while i < 10:
    if age > 20 and age < 40 and gender[i] != "Female":
        x.append(round(u(1.6,1.9),2))
        i += 1
    elif age > 20 and age < 40 and gender[i] != "Male":
        x.append(round(u(1.6,1.9),2))
        i += 1
    else:
        print("Hello")
        break
        

print(x)
print(gender)


#bug fix at gender logic (perhaps age)
#