from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for x in question_data:
    question_text = x["text"]
    question_answer = x["answer"]
    questione = Question(text=question_text,answer=question_answer)
    question_bank.append(questione)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
