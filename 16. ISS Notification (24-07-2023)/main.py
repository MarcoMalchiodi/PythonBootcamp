import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.464203
MY_LONG = 9.189982

my_email = "randomaddress@gmail.com"
my_password = "dASDsaezawenmpgbf"

# --------------------------- ISS LOCATION -------------------------- #
response = requests.get(url='http://api.open-notify.org/iss-now.json') #the URL is the API endpoint 
#print(response) returns Response [200] which is the response code

responde_code = response.status_code #returns an integer
response.raise_for_status() #if we don't get a 200 it will raise an exception

data = response.json() #it is treated like any dictionary
# ex. message = response.json()[key][sub-key]

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
current_position = (latitude,longitude)

# ----------------------------------- MY TIMEZONE ------------------- #
parameters = {
    'lat':MY_LAT,
    'lng':MY_LONG,
    'formatted':0,
}

response2 = requests.get('https://api.sunrise-sunset.org/json', params=parameters) #same as editing the link manually with ? and &'s
response2.raise_for_status()
data2 = response2.json()
sunrise = data2["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data2["results"]["sunset"].split('T')[1].split(':')[0]

time_now = datetime.now()
current_hour = time_now.hour


# ------------------------ COMPARISON ------------------------------- #
ISS_exists = True

while ISS_exists:
    time.sleep(60)
    if current_hour > sunset or current_hour < sunrise:
        if (abs(longitude-MY_LONG) <= 5) and (abs(latitude-MY_LAT) <= 5):
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs='poorvictim@gmail.com',msg='Subject:Watch outside!\n\nThe aliens are coming!')