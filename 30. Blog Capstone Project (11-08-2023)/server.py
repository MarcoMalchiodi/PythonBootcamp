from flask import Flask,render_template
import requests

blog_api='https://api.npoint.io/50e115850b8000ec52fa'
response=requests.get(blog_api)
response.raise_for_status()
data=response.json()

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def main_page():
    return render_template('index.html',blog_posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def read_post(id):
    post = None
    for x in data:
        if x['id']==id:
            post = x
    return render_template('post.html', blog_post=post)

if __name__ == '__main__':
    app.run()