from flask import Flask, render_template
import requests


app = Flask(__name__)

response=requests.get('https://api.npoint.io/c790b4d5cab58020d391')
posts=response.json()

@app.route('/')
def home():
    return render_template("index.html",blog_posts=posts)

@app.route('/<id>')
def read(id):
    blog_post=posts[int(id)-1]
    return render_template('post.html',post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)
