from tkinter import *
from quiz_brain import QuizBrain
import quiz_brain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quizzler'
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(bg='white', height=250, width=300)
        self.question_text = self.canvas.create_text(150,125, text='Question text', font=('Arial', 20,'italic'),fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)
        
        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, fg='white', font=('Arial', 14,'italic'))
        self.score_label.grid(column=1,row=0)
        
        true_image = PhotoImage(file='C:/Users/Marco/Desktop/project/images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0,command=self.check_right)
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file='C:/Users/Marco/Desktop/project/images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.check_wrong)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions:
            self.canvas.config(bg='white')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the question limit!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    
    def check_right(self):
       is_right = self.quiz.check_answer(user_answer='True')
       self.give_feedback(is_right)
    
    def check_wrong(self):
       is_right = self.quiz.check_answer(user_answer='False')
       self.give_feedback(is_right)

    def give_feedback(self, is_right):
        
        if is_right:
            self.canvas.config(bg='green')
            self.score +=1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg='red')
        
        self.window.after(1000, self.get_next_question)

            
        