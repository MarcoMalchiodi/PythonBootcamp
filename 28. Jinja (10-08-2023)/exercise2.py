from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response=requests.get(blog_url)
    data=response.json()
    return render_template('blog.html',posts=data)


@app.route('/<name>')
def home(name):
    return f'<p>Hello There {name}!</p>'

if __name__ == '__main__':
    app.run(debug=True)