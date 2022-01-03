import pandas as pd
from random import randint as rd

x = pd.read_csv(r"C:\Users\Adnan\Documents\World Cities\worldcities.csv")


num = rd(0,41001)
num1 = num + 49

if num1 >= 41001:
    num1 = num - 49

if num < num1:
    y = x["city"].loc[num:num1]
    yi = num
    yii = num1 + 1
else:
    y = x["city"].loc[num1:num]
    yi = num1
    yii = num + 1

cities = []
while yi < yii:
    cities.append(y.loc[yi])
    yi += 1

#print(cities)