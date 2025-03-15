import smtplib

my_email = "jincho1995@gmail.com"
password = "schasulseocpuypw"


# Send email

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, password)
    
    subject = "Hello from Python!"
    body = "This is a test email from Python."

    message = f"Subject: {subject}\n\n{body}"

    connection.sendmail(my_email, "rquesadaqq@outlook.com", message)



