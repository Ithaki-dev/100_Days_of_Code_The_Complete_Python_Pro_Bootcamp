import smtplib
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
my_email = "jincho1995@gmail.com"
password = "umhbybpdzcjuxcea"
connection.login(my_email, password)

# Send email

subject = "Hello from Python!"
body = "This is a test email from Python."

message = f"Subject: {subject}\n\n{body}"

connection.sendmail(my_email, "rquesadaqq@outlook.com", message)

connection.quit()

