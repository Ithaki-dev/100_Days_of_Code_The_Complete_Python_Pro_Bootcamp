from tkinter import *
import os


# Define the color scheme for the quiz app
THEME_COLOR = "#375362"
# Current path to the
current_path = os.path.dirname(__file__)
false_path = current_path+ "\\images\\false.png"
true_path = current_path+"\\images\\true.png"

# Create the quiz interface class
class QuizInterface:
    def __init__(self):
        # Window interface
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Score label
        self.score_label = Label(text="Score:", background=THEME_COLOR, font=("Arial",15,"italic"), fg="white")
        self.score_label.grid(column=1, row=0)
        
        # Question Canvas Text
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150,130,text="French", font=("Arial",20,"italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # True Button
        self.true_button_png = PhotoImage(file=true_path)
        self.true_button = Button(image=self.true_button_png, highlightthickness=0, background=THEME_COLOR)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        # False Button
        self.false_button_png = PhotoImage(file=false_path)
        self.false_button = Button(image=self.false_button_png, highlightthickness=0, background=THEME_COLOR)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()