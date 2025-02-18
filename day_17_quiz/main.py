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

while quiz.still_has_questions():
    question = quiz.next_question()
    print("\n")

print(f"You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")