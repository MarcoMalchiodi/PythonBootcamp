import requests
import datetime as dt


# -------------------------- SETTING UP EXERCISE DATA -------------- #
#NUTRION API USES POST
nutrition_id = 'db6ffFDSf8' #dummy id
nutrition_key = 'aggdsdgagasg4ecaf3aea' #dummy key
nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutrition_headers = {
    'x-app-id':nutrition_id,
    'x-app-key':nutrition_key
}

nutrition_params = {
    'query':input('What kind of exercise did you do today?'),
    'gender':'male',
    'weight_kg':79,
    'height_cm':185,
    'age':23
}

request = requests.post(url=nutrition_endpoint, headers=nutrition_headers,json=nutrition_params)
exercise_result = request.json()
print(request.text)


# ------------------------ CONNECTING TO SPREADSHEET ---------------- #
#SHEETY API USES GET TO RETRIEVE ROWS AND POST TO ADD NEW ONES

sheety_endpoint = 'https://api.sheety.co/3acda51cfSDFASDFSDAFSD8073203248/myDummy/dummies'

today = dt.datetime.now()

today_date = dt.datetime.now().strftime("%d/%m/%Y") #remember to add the '/
now_time = dt.datetime.now().strftime("%X")

for exercise in exercise_result['exercises']:
    sheet_inputs = {
        'dummies':{
            'date':today_date,
            'time':now_time,
            'exercise':exercise['name'].title(),
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories']
            
        }
    }
sheet_request = requests.post(url=sheety_endpoint, json=sheet_inputs)
print(sheet_request.text)