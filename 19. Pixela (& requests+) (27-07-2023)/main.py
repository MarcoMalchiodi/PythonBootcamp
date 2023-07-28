import requests
import datetime as dt

# requests.post() i the opposite of get(). We send data instead of retrieving it

# requests.put() is used to update a piece of data. ex. spreadsheets

pixel_endpoint = 'https://pixe.la/v1/users'

#step 1) Create a user

user_params = {
    'token':'12345678',
    'username':'mordechai',
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

"""response = requests.post(url=pixel_endpoint,json=user_params)
   print(response.text)
upon creating the response, we can comment it out since the user has already been created"""

TOKEN = user_params['token']
USERNAME = user_params['username']


#step 2) Create a graph

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id':'graph1',
    'name':'Cycling Graph',
    'unit':'Km',
    'type':'float',
    'color':'momiji'
}

http_headers = {
    'X-USER-TOKEN':TOKEN
}

#response = requests.post(url=graph_endpoint,json=graph_config,headers=http_headers)
#print(response.text)
#the graph can be found at https://pixe.la/v1/users/mordechai/graphs/graph1.html



#step 3) adding pixels to the graph

today = dt.datetime.now()

pixel_body = {
    'date':today.strftime('%Y%m%d'),
    'quantity':'35'
}

graph_endpoint = graph_endpoint +f"/{graph_config['id']}"

#response = requests.post(url=graph_endpoint,json=pixel_body,headers=http_headers)
#print(response.text)



#step 4) putting and deleting pixels

#response = requests.delete(url=graph_endpoint+f"/{today.strftime('%Y%m%d')}",headers=http_headers)

put_config = {
    'quantity':'35'
}
response = requests.put(url=graph_endpoint+f"/20230727", headers=http_headers, json=put_config)