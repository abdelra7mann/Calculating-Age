
# Software for Calculating-Age.py
#______________________________
import datetime
# User years input
years = input('years --  ')
years = int(years)
# User month input
month = input('month  --   ')
month = int(month)
# User days input
days = input('days  --   ')
days = int(days)
mybirthday = datetime.datetime(years,month,days)
now = datetime.datetime.now()
result = now - mybirthday
print (f'you lievd {result}  ')
