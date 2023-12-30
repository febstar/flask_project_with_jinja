from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    info = response.json()
    return render_template("index.html", info=info)

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    A = Post()
    info = A.get_post(blog_id)
    return render_template("post.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)
