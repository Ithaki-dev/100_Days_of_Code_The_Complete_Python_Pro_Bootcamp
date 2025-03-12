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

# Read the data file and select a random word
data = pd.read_csv(data_path)
random_french = ''
random_english = ''

def new_word():
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(card, image=card_front_png)
    random_french = random.choice(data["French"])
    random_english = data[data["French"] == random_french]["English"].iloc[0]
    print(random_french,random_english)
    canvas.itemconfig(word_text, text=random_french)

    
    window.after(3000, lambda: canvas.itemconfig(card, image=card_back_png))
    window.after(3000, lambda: canvas.itemconfig(language_text, text="English"))
    window.after(3000, lambda: canvas.itemconfig(word_text, text=random_english))
    return

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



# Rigth Button
rigth_button_png = PhotoImage(file=right_button_path)
rigth_button = Button(image=rigth_button_png, highlightthickness=0, command=new_word)
rigth_button.grid(row=1, column=0)

# Wrong Button
wrong_button_png = PhotoImage(file=wrong_button_path)
wrong_button = Button(image=wrong_button_png, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=2)


def handle_correct_answer():
    print("Correct!")







window.mainloop()


