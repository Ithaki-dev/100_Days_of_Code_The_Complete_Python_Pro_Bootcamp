from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    username = EmailField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Here you would typically check the username and password against a database
        print(f"Username: {username}, Password: {password}")
        if username == "admin@email.com" and password == "12345678":
            print("Login successful.")
            return redirect(url_for('success'))
        else:
            print("Login failed. Redirecting to denied page.")
            return redirect(url_for('denied'))
        
    return render_template('login.html', form=form)

@app.route("/denied")
def denied():
    return render_template('denied.html')

@app.route("/success")
def success():
    return render_template('success.html')



if __name__ == '__main__':
    app.run(debug=True)
