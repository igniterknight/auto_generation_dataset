import pandas as pd
from random import randint as rd
from pandas.core.algorithms import diff

columns = ["Frist Name","Last Name","Username","Age","Date of Birth","Gender","Phone Number","City","Heigth","Weight"]
ci = 0 #colunmn iterator

dict = {} #initializing the dictionary
"""
#Code to Produce Random String for the Name Column
#21 Consonants in x and z variables and 5 Vowels in y variable.
x = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'] 
y = ['a', 'e', 'i', 'o', 'u']
z = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

num = (int(input("Write number of Times to generated: ")))
lp = 1

while(lp <= num):
    xi = rd.randint(0,3)
    yi = rd.randint(0,4)
    zi = rd.randint(0,3)
    if lp <= num:
          string = "{a}{b}{c}e".format(a=x[xi],b=y[yi],c=z[zi])
          print(string)
          lp += 1
"""


"""
gen = ["Male","Female","Other"]

i = 0
while i < 10:
 geni = rd(0,2)
 print(gen[geni])
 i += 1

"""





l = []
j = 0


con = (int(input("Write down number of Columns[MAX 26]: ")))

while j < con:
    l.append(columns[ci])
    j += 1
    ci += 1

rows = (int(input("Write down number of Rows: ")))
dict = {}
x = len(l)
i = 0
v = 1

n = 1
m = rows + 1

while i < x:
    key = l[i]
    value = list(range(n,m))
    dict[key] = value
    i += 1
    n += 10
    m += 10
    
df = pd.DataFrame(dict)
df.index += 1
print(df)

"""

import random as rd

x = ["H","D","L","B"]
y = ["a","e","i","o","u"]
z = ["s","m","n","d"] 

num = (int(input("Write number of Times to generated: ")))
lp = 1

while(lp <= num):
    xi = rd.randint(0,3)
    yi = rd.randint(0,4)
    zi = rd.randint(0,3)
    if lp <= num:
          string = "{a}{b}{c}e".format(a=x[xi],b=y[yi],c=z[zi])
          print(string)
          lp += 1
        

import datetime
import random
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 2, 1) 

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)
print (type(random_date))

"""









