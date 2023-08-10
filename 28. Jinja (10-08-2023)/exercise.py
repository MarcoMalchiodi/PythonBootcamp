from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/<name>')
def home(name):
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data['age']
    
    response = requests.get(f'https://api.genderize.io?name={name}')
    response.raise_for_status()
    data = response.json()
    gender=data['gender']
    
    return render_template('exercise1.html',my_name=name, my_gender=gender,my_age=age)


if __name__ == '__main__':
    app.run()
