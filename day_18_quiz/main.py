#This is a Quiz game
from question_model import Question
from data import question_data

question_bank=[]

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    quiz = Question(text,answer)
    #print(text,answer)
    question_bank.append(quiz)

print(question_bank)