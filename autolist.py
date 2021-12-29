import pandas as pd
from pandas.core.algorithms import diff

columns = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
l = []
j = 0
ci = 0

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

