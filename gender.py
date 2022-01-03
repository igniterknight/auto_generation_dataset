from random import randint as rd
from citylist import cities
gender_list = ["Male","Female","Other"]
gender = []
i = 0
while i < 10:
 gi = rd(0,2)
 gender.append(gender_list[gi])
 i += 1

# print(gender)


