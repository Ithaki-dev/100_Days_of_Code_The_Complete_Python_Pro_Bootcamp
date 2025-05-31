from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

url_api = 'https://www.npoint.io/docs/3083c920e6d9c3d71c94'

# get the post infromation from the request
def get_posts():
    response = requests.get("https://api.npoint.io/3083c920e6d9c3d71c94")
    return response.json()

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/post/<int:post_id>')
def post(post_id):
    posts = get_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
