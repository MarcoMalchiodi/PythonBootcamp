from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    request_name = request.form['username']
    request_password = request.form['password']
    return render_template('login.html',name=request_name, password=request_password)
#it can also be dynamically generated with url_for e.g. <form action="{{ url_for('receive_data') }}" method="post">


if __name__ == '__main__':
    app.run()