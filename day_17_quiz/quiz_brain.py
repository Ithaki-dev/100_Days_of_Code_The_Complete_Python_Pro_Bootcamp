#this is the brain quiz

class QuizBrain():
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        
    
    ##def __str__(self):
    #    return f"Quiz Progress: {self.question_number}/{len(self.question_list)} | Score: {self.score}"
    

    def next_question(self):
        """This function retrieves the next question from the question list for the quiz.""" 
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {current_question.text} (True|False): ")
        
    