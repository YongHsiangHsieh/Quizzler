from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizUI:
    def __init__(self, quiz_bank: QuizBrain):
        self.quiz = quiz_bank

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Hello World", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_img = PhotoImage(file='images/true.png')
        self.check_but = Button(image=check_img, highlightthickness=0, command=self.true_pressed)
        self.check_but.grid(column=0, row=2)

        cross_img = PhotoImage(file='images/false.png')
        self.cross_but = Button(image=cross_img, highlightthickness=0, command=self.false_pressed)
        self.cross_but.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.check_but.config(state='disabled')
            self.cross_but.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(500, self.get_next_question)
