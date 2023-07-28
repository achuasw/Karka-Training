import pytz
from pytz import timezone
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
#from datetime import time
# current_date=date(2023,7,20)
# print(current_date)

current_date1=date.today()
# a=current_date1.year
# b=current_date1.month
# c=current_date1.day
#d=current_date1.weekday()
#print(d)
# print(a,b)
print(current_date1.weekday)

# new_year=date(2023,1,1)
# print((current_date1-new_year).days)




current_time1=time(9,56,45).hour
# print(current_time1,current_time2,current_time3)
current_time=time()
print(current_time)


# current_date_time=datetime.today()
# print(current_date_time)
# print(current_date_time.now())
# q=current_date_time.strftime("%y-%m-%d,%H:%M:%S")
# print(q)

# UTC=pytz.utc
# IST=pytz.timezone("asia/kolkata")
# print(current_date_time.now(UTC))
# print(current_date_time.now(IST))

# format="%d-%m-%Y %H:%M:%S %Z%z"
# utc=datetime.now(timezone("utc"))
# print(utc.strftime(format))
# asia=utc.astimezone(timezone("Asia/kolkata"))
# print(asia.strftime(format))

# a=datetime.now(pytz.timezone("Asia/kolkata"))
# print(a)


a="22 october 2002"
print(type(a))
format=("%d %B %Y")
b=datetime.strptime(a,format)
date1=b+timedelta(days=-5)
print(date1)
# print(type(b))
# print(b)

days=(input("Enter the days: "))
current_date=date.today()
format=("%d-%M-%Y")
c=datetime.strftime(current_date,format)
dates=c+timedelta(days=days)
print(dates)
# print(c)

# print(current_date)
