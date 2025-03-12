import random
from tkinter import *
import os
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# files paths
current_path = os.path.dirname(__file__)
card_front_path = current_path + "\\images\\card_front.png"
card_back_path = current_path + "\\images\\card_back.png"
right_button_path = current_path + "\\images\\right.png"
wrong_button_path = current_path + "\\images\\wrong.png"
data_path = current_path + "\\data\\french_words.csv"
learned_words_path = current_path + "\\data\\learned.csv"

# Read the data file and select a random word
data = pd.read_csv(data_path)
random_french = ''
random_english = ''

# Get random word from data 
def new_word():
    global random_english
    global random_french
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(card, image=card_front_png)
    random_french = random.choice(data["French"])
    random_english = data[data["French"] == random_french]["English"].iloc[0]
    print(random_french,random_english)
    canvas.itemconfig(word_text, text=random_french)

    window.after(30000, lambda: canvas.itemconfig(card, image=card_back_png))
    window.after(30000, lambda: canvas.itemconfig(language_text, text="English"))
    window.after(30000, lambda: canvas.itemconfig(word_text, text=random_english))
    return

# Remove the learned word from data.csv file
def remove_word():
    global data
    data = data[(data["French"] != random_french) | (data["English"] != random_english)]
    data.to_csv(data_path, index=False)
    print(f"{random_french} - {random_english} removed from data.csv")

# Save the word in csv file
def save_word():
    global data
    try:
        learned_words = pd.read_csv(learned_words_path)
        new_word_df = pd.DataFrame([{"French": random_french, "English": random_english}])
        learned_words = pd.concat([learned_words, new_word_df], ignore_index=True)
        learned_words.to_csv(learned_words_path, index=False)
        print(f"{random_french} - {random_english} saved in learned.csv")
        new_word()
    except FileNotFoundError:
        learned_words = pd.DataFrame(columns=["French", "English"])
        learned_words.to_csv(learned_words_path, index=False)
        save_word()

# Window
window = Tk()
window.title("Flashcard Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card front
card_front_png = PhotoImage(file=card_front_path)
card_back_png = PhotoImage(file=card_back_path)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_png)
language_text = canvas.create_text(400, 150,text="French", font=("Arial",30,"italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial",60,"bold"))
canvas.grid(row=0, column=0, columnspan=3)
new_word()

# Rigth Button
rigth_button_png = PhotoImage(file=right_button_path)
rigth_button = Button(image=rigth_button_png, highlightthickness=0, command=save_word)
rigth_button.grid(row=1, column=0)

# Wrong Button
wrong_button_png = PhotoImage(file=wrong_button_path)
wrong_button = Button(image=wrong_button_png, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=2)


window.mainloop()


