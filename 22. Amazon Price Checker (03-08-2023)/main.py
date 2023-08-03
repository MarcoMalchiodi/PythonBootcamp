#this short code is supposed to notify the user whenever an item on Amazon has hit the target price. It checks everyday twice a day
import requests
from bs4 import BeautifulSoup
import datetime as dt
import smtplib

TARGET_PRICE = 15.00
MY_URL = 'https://www.amazon.it/dp/1684224195/?coliid=I3GK46FVHN62YT&colid=1BQXQH445J2C9&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it_im'
current_date = dt.datetime.now()
hour = current_date.hour

my_headers= {
    'User-Agent':'randomUserAgent',
    'Accept-Language':'it,en-US;q=0.9,en;q=0.8'
}
website = requests.get(url=MY_URL,headers=my_headers)
content = website.text


soup = BeautifulSoup(content,'html.parser')
price = soup.find(name='span',id='price').getText()[:6]
price = float(price.replace(',','.'))
title = soup.find(name='span', id='productTitle').getText()

my_email = "randomaddress@gmail.com"
my_password = "hgasdhsrhhwrrth"

alert_message = f"Subject:Amazon Price Alert\n\nThe price of '{title}' has fallen below the target price! You can find it at {MY_URL}"

if hour == 9 or hour ==21:
    if price >= TARGET_PRICE:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls() #this line makes the connection secure by encrypting the mail
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=alert_message)

print(alert_message)



