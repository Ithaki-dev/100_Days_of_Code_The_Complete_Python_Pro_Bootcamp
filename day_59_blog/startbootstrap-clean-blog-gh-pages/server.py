from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/post')
def post(post_id):
    # In a real application, you would fetch the post from a database
    return render_template('post.html', post_id=post_id)

if __name__ == '__main__':
    app.run(debug=True)
