import smtplib
import datetime as dt
import random

now = dt.datetime.now()

year = now.year
month = now.month
weekday = now.weekday() #0 is monday
day = now.day
hour = now.hour

quotes = []
with open('quotes.txt', 'r') as file:
    all_quotes = file.readlines()
    for x in all_quotes:
        quotes.append(x)

my_email = "valerioalbini99@gmail.com"
my_password = "guouhezawenmpgbf"

app_password= "guouhezawenmpgbf" #birthday_wisher

if weekday==6:

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls() #this line makes the connection secure by encrypting the mail
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="hallowen872@gmail.com",msg=f'Subject:Quote of the Day\n\n{random.choice(quotes)}')
