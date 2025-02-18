#This is a Quiz game
from question_model import Question
from data import question_data

question_bank=[]

for data in question_data:
    question_bank.append(Question(data))

print(question_bank)