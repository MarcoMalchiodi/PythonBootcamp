from flask import Flask,render_template, request
import requests
import smtplib

blog_api='https://api.npoint.io/50e115850b8000ec52fa'
response=requests.get(blog_api)
response.raise_for_status()
data=response.json()

app = Flask(__name__)

my_email = "legitemailaddress@gmail.com"
my_password = "guouhezawenmpgbf"
def send_email(name,email,number,message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls() #this line makes the connection secure by encrypting the mail
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="somemail@gmail.com",msg=f"Name: {name}\nEmail: {email}\nTelephone number: {number}\nMessage: {message}")

@app.route('/index.html')
@app.route('/')
def main_page():
    return render_template('index.html',blog_posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method=='POST':
        email_address = request.form['email']
        username = request.form['name']
        phone_number = request.form['phone']
        user_message = request.form['message']
        send_email(name=username,email=email_address,number=phone_number,message=user_message)
        return render_template('contact.html',message_sent=True)
    
    return render_template('contact.html',message_sent=False)

@app.route('/post/<int:id>')
def read_post(id):
    post = None
    for x in data:
        if x['id']==id:
            post = x
    return render_template('post.html', blog_post=post)


    
    

if __name__ == '__main__':
    app.run()