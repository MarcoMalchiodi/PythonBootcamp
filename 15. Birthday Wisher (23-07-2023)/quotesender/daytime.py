import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
weekday = now.weekday() #0 is monday
day = now.day
hour = now.hour
minute = now.minute
second = now.second



#Creating a datetime object

date_of_birth = dt.datetime(year=1999,month=8,day=19)
print(date_of_birth)