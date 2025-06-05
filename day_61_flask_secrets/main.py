from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

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

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

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
        return redirect(url_for('success'))
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')



if __name__ == '__main__':
    app.run(debug=True)
