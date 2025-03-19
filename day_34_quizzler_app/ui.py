from tkinter import *
import os
from quiz_brain import QuizBrain


# Define the color scheme for the quiz app
THEME_COLOR = "#375362"
# Current path to the
current_path = os.path.dirname(__file__)
false_path = current_path+ "\\images\\false.png"
true_path = current_path+"\\images\\true.png"

# Create the quiz interface class
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window interface
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Score label
        self.score_label = Label(text="Score:", background=THEME_COLOR, font=("Arial",15,"italic"), fg="white")
        self.score_label.grid(column=1, row=0)
        
        # Question Canvas Text
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            130,
            width=280,
            text="Question",
            font=("Arial",18,"italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # True Button
        true_button_png = PhotoImage(file=true_path)
        self.true_button = Button(image=true_button_png, highlightthickness=0, background=THEME_COLOR,command=lambda: self.check_answer("true"))
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        # False Button
        false_button_png = PhotoImage(file=false_path)
        self.false_button = Button(image=false_button_png, highlightthickness=0, background=THEME_COLOR,command=lambda: self.check_answer("false"))
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text= q_text)

    def change_white(self):
        self.canvas.config(background="white")

    def check_answer(self, is_correct):
        answer = self.quiz.check_answer(is_correct)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        
        if answer is True:
            self.canvas.config(background="Green")
            self.window.after(2000, self.get_next_question)
            
      
        else:
            self.canvas.config(background="red")
            self.window.after(2000, self.get_next_question)
            
        self.window.after(2000, self.change_white)
        

        
     # Check if all questions are answered
        if self.quiz.still_has_questions():
            return
        # Close the window after finishing all questions
        self.window.quit()


    
