import tkinter

def calculate_km_distance():
    global my_label_conversion_rate, my_entry
    result = int(my_entry.get()) * 1.60934
    my_label_conversion_rate.config(text=result, font=("Arial", 16, "italic"))
    

# window title
window = tkinter.Tk()
window.title("Mile to kilometers")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)
# label miles 
my_label_miles = tkinter.Label(text="Miles", font=("Arial",16,"italic"))
my_label_miles.grid(column=2, row=0)
my_label_miles.config(padx=5, pady=5)

# label kilometers

my_label_kilometers = tkinter.Label(text="Km", font=("Arial",16,"italic"))
my_label_kilometers.config(padx=5, pady=5)
my_label_kilometers.grid(column=2, row=1)


# label conversion rate

my_label_conversion_rate = tkinter.Label(text="1 mile = 1.60934 kilometers", font=("Arial",12,"italic"))
my_label_conversion_rate.config(padx=5, pady=5)
my_label_conversion_rate.grid(column=1, row=1)

# label is eaqual to

my_label_is_equal_to = tkinter.Label(text="is equal to", font=("Arial",16,"italic"))
my_label_is_equal_to.config(padx=5, pady=5)
my_label_is_equal_to.grid(column=0, row=1)

# Button
my_button = tkinter.Button(text="Click me", command=calculate_km_distance)
my_button.config(padx=5, pady=5)
my_button.grid(column=1, row=2)

# entry miles
my_entry = tkinter.Entry(window)
my_entry.config(width=20)
my_entry.grid(column=1, row=0)





window.mainloop()

