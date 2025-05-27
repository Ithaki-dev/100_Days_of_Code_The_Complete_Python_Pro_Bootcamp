from flask import Flask

app = Flask(__name__)\

class Styler:
    @staticmethod
    def bold(func):
        def wrapper(*args, **kwargs):
            return f"<strong style='color: red;'>{func(*args, **kwargs)}</strong>"
        return wrapper

    @staticmethod
    def emphasize(func):
        def wrapper(*args, **kwargs):
            return f"<em style='color: green;'>{func(*args, **kwargs)}</em>"
        return wrapper

    @staticmethod
    def underline(func):
        def wrapper(*args, **kwargs):
            return f"<u style='color: blue;'>{func(*args, **kwargs)}</u>"
        return wrapper

bold = Styler.bold
emphasize = Styler.emphasize
underline = Styler.underline

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated(user):
    def wrapper(*args, **kwargs):
        if user.is_logged_in:
            return args[0](*args, **kwargs)
        else:
            print("User is not authenticated.")
            return "Access denied."


@is_authenticated        
def create_blog_post(user):
    print(f"Blog post created by {user.name}")


@app.route("/")
def hello_world():
    return "<div style='text-align:center;'><h1 style='color:blue;'>Hello, World!</h1>" \
    "<p>Welcome to my Flask app!</p>" \
    "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTU5Z3F2b3I3N3k4b2ZyMGluOTJ1Ynp2MnE1am9vY245YTg1NmExeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uX7EYxL3hhXoX6hK0N/giphy.gif' alt='Placeholder Image'></div>"

@app.route("/greet/<name>")
def greet(name):
    return f"<div style='text-align:center;'><h1 style='color:green;'>Hello, {name}!</h1></div>"

@app.route("/bye")
@bold
@emphasize
@underline
def bye():
    return "bye!"

if __name__ == "__main__":
    app.run(debug=True)

    # Test user authentication
    new_user = User("Robert")
    new_user.is_logged_in = True
    create_blog_post(new_user)  # Should print: Blog post created by Robert