from tkinter import *
from tkinter import ttk
import os
import time

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
def countdown():
    count_down_seconds = 5
    while count_down_seconds > 0:
        canvas.itemconfig(timer_text, text=f"{count_down_seconds:02d}")
        window.update()
        time.sleep(1)
        count_down_seconds -= 1
    # after timer is up, make a short break
    canvas.itemconfig(timer_text, text="Break")
    window.update()
    time.sleep(SHORT_BREAK_MIN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=25, pady=25, bg=YELLOW, highlightthickness=0) 
current_path = os.path.dirname(__file__)
canvas =  Canvas(width=200, height=224, bg=YELLOW)
bg_image = PhotoImage(file=current_path+"\\tomato.png")
canvas.create_image(103,112, image=bg_image)
#canvas.create_text(103,112, text="00:00",fill ="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


#TIMER TEXT
timer_text = canvas.create_text(103, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

#TIMER LABEL
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
timer_label.grid(column=1, row=0)

#START BUTTON
start_button = Button(text="Start", font=(FONT_NAME, 15), bg=YELLOW, highlightthickness=0, command=countdown)
start_button.grid(column=0, row=2)

#RESET BUTTON
reset_button = Button(text="Reset", font=(FONT_NAME, 15), bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

#LABEL CHECKMARK
checkmark_label = Label(text="✓", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(column=1, row=3)



window.mainloop()