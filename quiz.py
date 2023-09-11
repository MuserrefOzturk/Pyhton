class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions=questions
        self.score=0
        self.qindex=0
    def getQuestion(self):
        return self.questions[self.qindex]
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Question {self.qindex +1}: {question.text}')

        for q in question.choices:
            print('-'+ q)
        
        answer= input('answer: ')
        self.guess(answer)
    
    def guess(self,answer):
        question=self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score +=1
        self.qindex +=1

        self.displayQuestion()
    
q1= Question('The best program language?',['c#','python','js','java'],'python')
q2= Question('The most popular program language?',['c#','js','java','python'],'python')
q3= Question('The easiest program language?',['c#','js','python','java'],'python')
questions=[q1,q2,q3]
quiz=Quiz(questions)
quiz.displayQuestion()






#print(q1.checkAnswer('python'))
#print(q2.checkAnswer('c#'))