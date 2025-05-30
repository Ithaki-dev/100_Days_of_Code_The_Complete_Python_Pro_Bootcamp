from flask import Flask, render_template
import requests

def get_posts():
    response = requests.get("https://api.npoint.io/3083c920e6d9c3d71c94")
    return response.json()

app = Flask(__name__)

posts = get_posts()

@app.route('/')
def home():
    """
    Render the home page with a list of blog posts.

    The `posts` variable contains data fetched from an external API
    and is passed to the template for rendering.
    """
    return render_template("index.html", posts=posts)

from flask import request

@app.route('/blog')
def get_blog():
    """
    Handles requests to the '/blog' route.

    Retrieves a specific blog post based on the 'post_id' query parameter.
    The 'post_id' is expected to be an integer. If no matching post is found 
    or if 'post_id' is invalid, the function returns None and renders the 
    'post.html' template with an empty post.
    """
    post_id = request.args.get('post_id')
    requested_post = None
    if post_id:
        try:
            post_id = int(post_id)
            for post in posts:
                if post["id"] == post_id:
                    requested_post = post
                    break
        except ValueError:
            requested_post = None
    return render_template("post.html", requested_post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
