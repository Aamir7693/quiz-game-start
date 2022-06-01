from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
Question_Bank=[]
for dict in question_data:
    Question_Bank.append(Question(dict['text'],dict['answer']))
quiz=QuizBrain(Question_Bank)
quiz.next_question()
