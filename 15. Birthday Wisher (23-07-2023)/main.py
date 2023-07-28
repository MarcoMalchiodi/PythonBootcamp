import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day
my_email = "randomaddress@gmail.com"
my_password = "hgasdhsrhhwrrth"


data = pandas.read_csv('birthdays.csv')

data_names = data['name'].to_list()
data_email = data['email'].to_list()
data_month = data['month'].to_list()
data_day = data['day'].to_list()


def send_letter(letter, email, name):
    
    with open(letter,'r') as file_template:
        template = file_template.read()
    
    old_word = "[NAME]"
    my_letter = template.replace(old_word, name)
        
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls() #this line makes the connection secure by encrypting the mail
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=email,msg=my_letter)
        
    


for x in range(len(data_month)):
    if data_month[x-1]==month:
        if data_day[x-1]==day:
            chosen_letter = f'letter_{random.randint(1,3)}.txt'
            send_letter(letter=chosen_letter,email=data_email[x-1],name=data_names[x-1])
        






