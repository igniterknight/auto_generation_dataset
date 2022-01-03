from dateutil.relativedelta import relativedelta
from datetime import date
import dob
rdelta = relativedelta(date.today(), dob.dates)
age = rdelta.years
#print ('Age in months - ', rdelta.months)
# print ('Age in days - ', rdelta.days)
