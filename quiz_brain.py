
class QuizBrain:
    def __init__(self,dict):
        self.question_no=0
        self.question=dict
        self.score=0
    def next_question(self):
        stop=len(self.question)
        iter=0
        while(iter<stop):
            current=self.question[self.question_no]
            inp=input(f"Q{self.question_no+1}.{current.text} (True/False)")
            self.question_no+=1
            if inp==current.answer:
                iter+=1
                self.score+=1
            else:

                print(f"Wrong answer !! your Score is : {self.score} ")

