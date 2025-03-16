import random
import smtplib
import datetime as dt
import os

my_email = "jincho1995@gmail.com"
password = "kmbazakibbrqchgg"
current_path = os.path.dirname(__file__)
quote_text_path = current_path+"\\quote.txt"

# Send email
def send_email( email, password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        
        subject = "Have a nice day"
        body = get_quote()
        message = f"Subject: {subject}\n\n{body}".encode('utf-8')

        connection.sendmail(email, "rquesadaqq@outlook.com", message)

# Read quote from file and return a random quote

def get_quote():
    try:
        with open(quote_text_path, "r", encoding="utf-8") as file:
            quotes = file.readlines()
            quote = random.choice(quotes)
            return quote
    except FileNotFoundError:
        return "Error: Could not find the quote file."


current_time = dt.datetime.now()
week_day = current_time.weekday()
print(week_day)
if week_day == 5:
    send_email(my_email, password)