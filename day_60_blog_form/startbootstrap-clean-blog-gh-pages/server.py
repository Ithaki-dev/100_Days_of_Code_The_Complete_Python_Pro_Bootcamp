from flask import Flask, render_template, request, redirect, url_for
import requests
import smtplib

app = Flask(__name__)

url_api = 'https://www.npoint.io/docs/3083c920e6d9c3d71c94'
my_email = "your@gmail.com"
my_password = "yourpassword"  # Replace with your actual password

# get the post infromation from the request
def get_posts():
    response = requests.get("https://api.npoint.io/3083c920e6d9c3d71c94")
    return response.json()

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    posts = get_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

@app.route('/contact', methods=['POST'])
def contact_post():
    # Handle the form submission
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    print(f"Received contact form submission: {name}, {email}, {phone}, {message}")
    #Send an email with the contact information
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            # Create the email message
            email_message = (f"Subject:New Contact Form Submission\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}").encode('utf-8')
            connection.sendmail(
                from_addr=my_email,
                to_addrs="yoursender@outlook.com",
                msg=email_message
            )
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
