from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    question_text: int

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white', )
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='Some question text',
            fill=THEME_COLOR,
            font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.configure(text =f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def click_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def click_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right:bool):
        if is_right:
            self.canvas.configure(bg='green')
        else :
            self.canvas.configure(bg='red')

        self.window.after(ms=1000, func=self.get_next_question)


