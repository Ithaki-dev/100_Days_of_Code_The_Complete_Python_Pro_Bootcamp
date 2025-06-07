from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, URLField
from wtforms.validators import DataRequired
import csv
import os


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
current_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap =Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField('Location URL', validators=[DataRequired()])
    open_time = StringField('Open time', validators=[DataRequired()])
    closing_time = StringField('Closing time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating (1-5)', validators=[DataRequired()], choices=[
        ('✘'),
        ('☕️'),
        ('☕️☕️'),
        ('☕️☕️☕️'),
        ('☕️☕️☕️☕️'),
        ('☕️☕️☕️☕️☕️')
    ], default='☕️')
    wifi_rating = SelectField('Wifi rating (1-5)', validators=[DataRequired()], choices=[
        ('✘'),
        ('💪'),
        ('💪💪'),
        ('💪💪💪'),
        ('💪💪💪💪'),
        ('💪💪💪💪💪')
    ], default='💪')
    power_outlet_rating = SelectField('Power outlet rating (1-5)', validators=[DataRequired()], choices=[
        ('✘'),
        ('🔌'),
        ('🔌🔌'),
        ('🔌🔌🔌'),
        ('🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌')
    ], default='🔌')
    submit = SubmitField('Add Cafe')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add' , methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()    

    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location_url = form.location_url.data
        open_time = form.open_time.data
        closing_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_outlet_rating = form.power_outlet_rating.data
        
        with open(current_path + '/cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([cafe_name, location_url, open_time, closing_time, coffee_rating, wifi_rating, power_outlet_rating])
        
        return render_template('index.html')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(current_path + '/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
