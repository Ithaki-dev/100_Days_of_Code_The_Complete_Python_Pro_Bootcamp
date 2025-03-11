from tkinter import *
import os

BACKGROUND_COLOR = "#B1DDC6"

current_path = os.path.dirname(__file__)
card_front_path = current_path + "\\images\\card_front.png"

window = Tk()
window.title("Flashcard Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_png = PhotoImage(file=card_front_path)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_png)
canvas.create_text(400, 150,text="Title", font=("Arial",30,"italic"))
canvas.create_text(400, 263, text="Definition", font=("Arial",60,"bold"))
canvas.grid(row=0, column=0, columnspan=1)

# # Label title
# title_label = Label(text="Flashcard App", font=("Arial", 40, "italic"))
# title_label.grid(row=0, column=0, columnspan=1)

# #  Label word
# word_label = Label(text="Word", font=("Arial", 30, "bold"))
# word_label.grid(row=1, column=0, columnspan=1)








window.mainloop()


