from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=25, pady=25, bg=YELLOW, highlightthickness=0) 
current_path = os.path.dirname(__file__)

canvas =  Canvas(width=200, height=224, bg=YELLOW)
bg_image = PhotoImage(file=current_path+"\\tomato.png")
canvas.create_image(103,112, image=bg_image)
canvas.create_text(103,112, text="00:00",fill ="white", font=(FONT_NAME,35,"bold"))
canvas.pack()

window.mainloop()