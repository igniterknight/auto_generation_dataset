import pandas as pd
from random import randint as rd
from pandas.core.algorithms import diff
from datetime import date 
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from random import uniform as u
import random as rand

#columns = ["Frist Name","Last Name","Username","Email","Date of Birth","Age","Gender","Heigth","Weight","Phone Number","City","Country","Password"]

#-------------------------------------------
df = pd.read_csv(r'auto_P2\names.csv')
def first_name(a):
    fn1 = 0
    fn = []
    while fn1 < a:
            l = rd(0,6782)
            fn.append(df["Names"].loc[l])
            fn1 += 1
    return fn

def last_name(a):        
    ln1 = 0
    ln = []
    while ln1 < a:
        x = rd(3387,3470)         
        ln.append(df["Names"].loc[x])
        ln1 += 1                 
    return ln

#------------------------------------------------

start = date(1985,1,1)
end = date(2015,12,31)
x = end - start
days = x.days

def dob(a):
    i = 0
    global dobs
    dobs = []
    while i < a:
        random = rand.randrange(days)
        dates = start + timedelta(random)
        dobs.append(dates)
        i += 1
    return dobs

#------------------------------------------------

x = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z",'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
y = ["a","e","i","o","u"]
z = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z",'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'] 
q = list(range(50,551))


def username(a):
    lp = 0
    usr = []
    while(lp < a):
        xi = rd(0,41)
        yi = rd(0,4)
        zi = rd(0,41)
        qi = rd(50,500)
        string = (x[xi] + y[yi] + z[zi] + str(q[qi]))
        usr.append(string)
        lp += 1
    return usr


#------------------------------------------------

def age(a):
    global ages
    ages = []
    i = 0 
    while i < a:
        rdelta = relativedelta(date.today(),db[i])
        ages.append(rdelta.years)
        i += 1
    return ages 

#-----------------------------------------------

mgender = ["Male","Other"]
fgender = ["Female","Other"]

def gender(a):
    gen = []
    gi = 0
    while gi < a:
        if df.loc[df['Names'] == fn[gi], 'Gender'].iloc[0] == 'boy':
            x = rd(0,1)
            gen.append(mgender[x])
        else:
            x = rd(0,1)
            gen.append(fgender[x])
        gi += 1
    return gen

#------------------------------------------------

m1 = round(u(110.8,133.5),2)
m2 = round(u(137.2,169.4),2)
m3 = round(u(165.3,210.8),2)
m4 = round(u(175.4,215.9),2)
m5 = round(u(169.6,201.7),2)
m6 = round(u(165.9,191.3),2)

f1 = round(u(108.5,134.3),2)
f2 = round(u(142.9,156.2),2)
f3 = round(u(159.8,203.9),2)
f4 = round(u(163.2,206.2),2)
f5 = round(u(154.6,199.3),2)
f6 = round(u(151.7,187.4),2)

def height(a):
    height =[]
    i = 0
    while i < a:
        if ag[i] < 11 and gen[i] != "Female":
            height.append(m1)
            i += 1
        elif ag[i] > 10 and ag[i] < 16 and gen[i] != "Female":
            height.append(m2)
            i += 1
        elif ag[i] > 15 and ag[i] < 26 and gen[i] != "Female":
            height.append(m3)
            i += 1    
        elif ag[i] > 25 and ag[i] < 41 and gen[i] != "Female":
            height.append(m4)
            i += 1
        elif ag[i] > 40 and ag[i] < 60 and gen[i] != "Female":
            height.append(m5)
            i += 1
        elif ag[i] > 59 and gen[i] != "Female":
            height.append(m6)
            i += 1
        elif ag[i] < 11 and gen[i] != "Male":
            height.append(f1)
            i += 1
        elif ag[i] > 10 and ag[i] < 16 and gen[i] != "Female":
            height.append(f2)
            i += 1
        elif ag[i] > 15 and ag[i] < 26 and gen[i] != "Male":
            height.append(f3)
            i += 1    
        elif ag[i] > 25 and ag[i] < 41 and gen[i] != "Male":
            height.append(f4)
            i += 1
        elif ag[i] > 40 and ag[i] < 60 and gen[i] != "Male":
            height.append(f5)
            i += 1
        elif ag[i] > 59 and gen[i] != "Male":
            height.append(f6)
            i += 1
    return height

#------------------------------------------------



def number(a):
    i = 1
    y = [rd(6000000000,9999999999)]
    while i < a:
        l = rd(6000000000,9999999999)
        if l in y:
            continue
        else:
            y.append(l)
            i += 1               
    return y

#-------------------------------------------------

dt = pd.read_csv(r"auto_P2\city.csv")
t = dt["city"].loc[0:99]
    

def city(a):
    global cities
    cities = []
    c = 0
    while c < a: 
        num = rd(0,99)
        cities.append(t.loc[num])
        c += 1
    return cities 

def country(a):
    country = []
    c = 0
    while c < a: 
        x = dt.loc[dt['city'] == cities[c], 'country'].iloc[0]
        country.append(x)
        c += 1
    return country

#------------------------------------------------

x = [rd(0,1001)]
y = ['A','B', 'C', 'D','E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N',' O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W', 'X', 'Y', 'Z','b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z','a', 'e', 'i', 'o', 'u']
z = [rd(0,50),rd(0,34),rd(0,345)]
r = ['A',' B', 'C', 'D',' E', 'F', 'G', 'H',' I', 'J', 'K', 'L', 'M', 'N',' O', 'P', 'Q', 'R', 'S', 'T',' U',' V', 'W', 'X', 'Y', 'Z']
n = [rd(9748,9976)]




lis = []

def password(num):
    lp = 0
    while(lp < num):
        xi = 0
        yi = rd(0,52)
        zi = rd(0,2)
        ri = rd(0,26)
        ni = 0 
        if lp <= num:
            s = "{a}".format(a = str(x[xi] + y[yi] + str(z[zi]) + r[ri] + str(n[ni])) )
            lis.append(s)
            lp += 1
    return lis

#------------------------------------------------------------
row = (int(input("Write Number of Rows: ")))
fn = first_name(row)
w = last_name(row)
e = username(row)
db = dob(row)
ag = age(row)
gen = gender(row)
he = height(row)
no = number(row)
cc = city(row)
ct = country(row)
pas = password(row)

columns = ["Frist Name","Last Name","Username","Date of Birth","Age","Gender","Heigth","Phone Number","City","Country","Password"]
values = [fn,w,e,db,ag,gen,he,no,cc,ct,pas]

i = 0 
dict = {}

while i < 11:
    dict[columns[i]] = values[i]
    i += 1

dl = pd.DataFrame.from_dict(dict, orient='index')
dl = dl.transpose()
dl.index += 1
print(dl)