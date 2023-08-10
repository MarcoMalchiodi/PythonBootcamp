#templating with Jinja
from flask import Flask, render_template
import random
import datetime

today = datetime.datetime.today()
current_date=today.strftime('%Y %m %d')

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, date=current_date)

if __name__ == "__main__":
    app.run(debug=True)


