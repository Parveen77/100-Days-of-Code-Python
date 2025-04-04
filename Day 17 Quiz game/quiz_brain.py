class QuizBrain:
    
    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.question_list = q_list
        
    def still_has_question(self):
        return self.q_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number +=1
        
        user_answer = input(f"Q. {self.q_number} {current_question.text} (True/False): ")
        #user_answer = True
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
            print(f"Your score is {self.score}/{self.q_number}")
        else: 
            print("That was wrong.")
            print(f"The correct answer was {correct_answer}")
            print(f"Your score is {self.score}/{self.q_number} \n")