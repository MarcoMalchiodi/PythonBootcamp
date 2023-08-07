from flask import Flask


app= Flask(__name__)

import random
print(random.__name__) #simply returns the name of the module ('random')
print(__name__) #returns '__main__', the file being currently run



@app.route('/')
def hello_world():
    return "<p>Hello, There!</p>"
#the @ sign is a python decorator


if __name__ == '__main__':  #this allows us to skip the initial procedure
    app.run()