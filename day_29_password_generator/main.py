import os
import random
import string
from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Initialize current path
current_path = os.path.dirname(__file__ )
def generate_password():
    password_entry.delete(0,END)
    letters = string.ascii_letters + string.digits + ".-_$*()#@!%/"
    password = ''.join(random.choice(letters) for i in range(10))
    password_entry.insert(0, password)
    password_entry.focus()

# ----------------------------SEARCH WEBSITE ------------------------------- #
def search_website():
    website = website_entry.get()

    try:
        with open(current_path + "\\data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title=website, message="No saved data for this website.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    #save info into a json file
    try:
        with open(current_path + "\\data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[website] = {
        "email": email,
        "password": password
    }

    with open(current_path + "\\data.json", "w") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo(title="Saved Password", message="Password saved successfully!")
    # Clear the text boxes
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
logo_path = current_path + "\\logo.png"
logo_png = PhotoImage(file=logo_path)
canvas =  Canvas(width=200, height=200)
canvas.create_image(10,10, image=logo_png, anchor="nw")
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

# Search website Button
search_button = Button(text="Search", width=15, command=search_website)
search_button.grid(column=2, row=1)

# Email/Username label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Email/Username entry
email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0,"rquesada@outlook.com")

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password entry
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, sticky="w")

# Generate password button
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

# Save password button
save_password_button = Button(text="Save Password", width=35, command=save_password)
save_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()