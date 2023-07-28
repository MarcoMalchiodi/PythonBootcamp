import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
Alert = False

stock_key = 'HFSDFSDTDX55OH87'
stock_json = 'https://www.alphavantage.co/query'
stock_parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':stock_key
}
new_key = '7cfbofebu40ba88ec9647da93147e'
news_json = 'https://newsapi.org/v2/everything'
news_parameters = {
    'q':COMPANY_NAME,
    'apiKey':new_key,
    'language':'en',
    'sortBy':'popularity',
}

# -------------------------- EXTRACTING STOCK PRICES DATA ------------ #

stock_request = requests.get(stock_json,params=stock_parameters)
stock_request.raise_for_status()
stock_data = stock_request.json()
first_index = list(stock_data['Time Series (Daily)'].keys())[0]
second_index = list(stock_data['Time Series (Daily)'].keys())[1]
last_close = float(stock_data['Time Series (Daily)'][first_index]['4. close'])
previous_close = float(stock_data['Time Series (Daily)'][second_index]['4. close'])

change_in_price = (round(last_close-previous_close,3))
percantage_in_change = (round(change_in_price/previous_close, 3))*100

if percantage_in_change >= 5:
    Alert = True


# -------------------------- EXTRACTING GLOBAL NEWS -------------- #

news_request = requests.get(news_json,params=news_parameters)
news_request.raise_for_status()
news = news_request.json()

titles = []
descriptions = []

bob = 0
for article in news["articles"]:
    titles.append(article['title'])
    descriptions.append(article['description'])
    bob +=1
    if bob >= 5:
        break
    
    
# -------------------------- Twilio -------------------- #

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "aadv43t3fed7d88deb71649346f1cc"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

for x in range(len(titles)):
    message = client.messages.create(
        to="+15558675309", 
        from_="+15017250604",
        body=f"{COMPANY_NAME}{percantage_in_change}\nHeadline:{titles[x-1]}\nBrief:{descriptions[x-1]}")


