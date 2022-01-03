from datetime import date 
from datetime import timedelta
import random as rd

start = date(1990,1,1)
end = date(2010,12,31)
x = end - start
days = x.days
random = rd.randrange(days)
dates = start + timedelta(random)
#print(dates)