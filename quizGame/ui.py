from re import I
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = Label(text=f"Score: 0", bg=THEME_COLOR, font=("Arial", 15, "normal"), fg="white")
        self.lbl_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR, font=("Arial", 20, "italic"), text="Test", width="280")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        

        btn_true_image = PhotoImage(file="100DaysOfCoding/quizGame/images/true.png")
        self.btn_true = Button(image=btn_true_image, highlightthickness=0, command=self.ans_true)
        self.btn_true.grid(row=2, column=0)

        btn_false_image = PhotoImage(file="100DaysOfCoding/quizGame/images/false.png")
        self.btn_false = Button(image=btn_false_image, highlightthickness=0, command=self.ans_false)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def ans_true(self):
        self.feedback(self.quiz.check_answer("True"))


    def ans_false(self):
        self.feedback(self.quiz.check_answer("False"))


    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)