import math
from tkinter import *
from tkinter import ttk
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
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(timer)
    REPS = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60
    if REPS % 4 == 0:
        countdown(long_break_sec)
        # update timer_label with "long break"
        timer_label.config(text="Break", fg=RED)
        
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        # update timer_label with "short break"
        timer_label.config(text="Break", fg=PINK)
        
    else:
        countdown(work_sec)
        # update timer_label with "work"
        timer_label.config(text="Work", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes, seconds = divmod(count, 60)
    time_format = "{:02d}:{:02d}".format(minutes, seconds)
    canvas.itemconfig(timer_text, text=time_format)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        #check every 2 reps add a checkmark using checkmark_label
        if REPS % 2 == 0:
            mark = ''
            work_sesions =math.floor(REPS/2)
            for i in range(work_sesions):
                mark += '✓'
            checkmark_label.config(text=mark)
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=25, pady=25, bg=YELLOW, highlightthickness=0) 
current_path = os.path.dirname(__file__)
canvas =  Canvas(width=200, height=224, bg=YELLOW)
bg_image = PhotoImage(file=current_path+"\\tomato.png")
canvas.create_image(103,112, image=bg_image)
canvas.grid(column=1,row=1)

#TIMER TEXT
timer_text = canvas.create_text(103, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

#TIMER LABEL
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
timer_label.grid(column=1, row=0)

#START BUTTON
start_button = Button(text="Start", font=(FONT_NAME, 15), bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#RESET BUTTON
reset_button = Button(text="Reset", font=(FONT_NAME, 15), bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

#LABEL CHECKMARK
checkmark_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(column=1, row=3)

window.mainloop()