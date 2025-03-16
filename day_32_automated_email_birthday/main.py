import random
import smtplib
import datetime as dt
import os
import pandas as pd

# Variables to store email and password and paths
my_email = "jincho1995@gmail.com"
password = "kmbazakibbrqchgg"
current_path = os.path.dirname(__file__)
letter_path = current_path + "\\letter_templates\\"
birthday_path = current_path + "\\birthdays.csv"

# Send email
def send_email( email, password, friend_name, friend_email):
    # Get a list of all letter template files
    letter_files = os.listdir(letter_path)
    # Select a random letter template file
    random_letter_file = random.choice(letter_files)
    # Open the selected letter template file and read its contents
    with open(letter_path + random_letter_file, 'r') as file:
        letter_template = file.read()
    # Replace the "[DEAR]" placeholder with the recipient's name
    modified_letter = letter_template.replace("[NAME]", friend_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        subject = "Happy Birthday"
        message = f"Subject: {subject}\n\n{modified_letter}".encode('utf-8')
        connection.sendmail(email, friend_email, message)

# Check who have a birthday today and return the name and email
def get_birthday_recipients():
    # Load the birthdays.csv file into a DataFrame
    birthdays_df = pd.read_csv(birthday_path)  
    # Get month
    current_month = dt.datetime.now().month  
    # Get day
    current_day = dt.datetime.now().day
    # Filter birthdays for the current month and day
    birthday_recipients = birthdays_df[(birthdays_df["month"] == current_month) & (birthdays_df["day"] == current_day)]
    # Save name and email into variables
    recipients_name = birthday_recipients["name"].to_string(index=False)
    recipients_email = birthday_recipients["email"].to_string(index=False)
    # Return the recipient's name and email
    return recipients_name, recipients_email

# Get recipient's name and email and send the birthday email
friend_name, friend_email = get_birthday_recipients()
send_email(my_email, password, friend_name, friend_email)