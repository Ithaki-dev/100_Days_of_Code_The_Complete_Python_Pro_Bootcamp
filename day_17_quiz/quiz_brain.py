#this is the brain quiz

class QuizBrain():
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        
    
    ##def __str__(self):
    #    return f"Quiz Progress: {self.question_number}/{len(self.question_list)} | Score: {self.score}"
    

    def next_question(self):
        """This function retrieves the next question from the question list for the quiz.""" 
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True|False): ")
        self.check_answer(user_answer, current_question.text)
        
    def still_has_questions(self):
        """This function checks if there are still questions left in the question list."""
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        """This function checks if the user's answer is correct and returns a boolean value."""

        correct_answer = self.question_list[self.question_number - 1].answer.lower()
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
            print(f"Current score:{self.score}/{self.question_number} points")
            return True
        else:
            print("Incorrect! The correct answer was:", correct_answer)
            print(f"Current score:{self.score}/{self.question_number} points")
            return False
        
    
    