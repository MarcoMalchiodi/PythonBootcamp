class QuizBrain:
    def __init__(self, listo):
        self.question_number = 0
        self.question_list = listo
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(print(f"Q.{self.question_number}. {current_question.text}   (True/False)"))
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, current_question):
        if user_answer == current_question:
            print("Correct!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}")
            print("\n")
        else:
            print("Wrong!")
            print("\n")
        
    
    def still_has_questions(self):
        limit = len(self.question_list)
        if self.question_number >= limit:
            print(f"\nYour total score was {self.score}/{limit}")
            return False
        else:
            return True
    

        