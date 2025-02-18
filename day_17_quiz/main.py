#This is a Quiz game
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    quiz = Question(text,answer)
    #print(text,answer)
    question_bank.append(quiz)

quiz = QuizBrain(question_bank)
quiz.next_question()
