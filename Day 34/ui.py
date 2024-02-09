from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain ):#Better to handle the types
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler') 
        self.window.config(padx = 20, pady=20, bg=THEME_COLOR)
        self.label =  Label(text="Score :0", bg=THEME_COLOR, foreground="white")
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width = 300,height = 250,highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Hello" , 
            fill=THEME_COLOR, 
            font=("Arial",20,"italic")) 
        self.canvas.grid(row=1,column=0,columnspan=2, padx=20,pady=50)

        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")
   
        self.wrong_button = Button(image=wrong,bg=THEME_COLOR, command=self.false_execute)
        self.wrong_button.grid(row=2, column=0)

        self.right_button = Button(image=right,bg=THEME_COLOR, command=self.true_execute)
        self.right_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='''You've reached the end of the Quiz''')
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_execute(self):
        check = self.quiz.check_answer('True')
        self.give_feedback(check)
        self.label.config(text = f"Score:{self.quiz.score}")
    
    def false_execute(self):
        check = self.quiz.check_answer('False')
        self.give_feedback(check)
        self.label.config(text = f"Score:{self.quiz.score}")
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
    
            