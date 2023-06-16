from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.config(padx=20, pady=20)
        self.score_label.grid(row=1, column=2)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.button_true = Button(image=true_img, highlightthickness=0, command=self.true_clicked)
        self.button_true.grid(row=3, column=1)
        self.button_false = Button(image=false_img, highlightthickness=0, command=self.false_clicked)
        self.button_false.grid(row=3, column=2)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Ariel", 20, "italic"), width=300)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)
        self.quiz = quiz
        self.put_question()
        self.window.mainloop()

    def put_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        else:
            self.quiz_end()

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.put_question)

    def quiz_end(self):
        self.canvas.itemconfig(self.canvas_text, text=f"You've completed the quiz. Your final score was: {self.quiz.score}/{self.quiz.question_number}")
        self.button_true.config(state="disabled")
        self.button_false.config(state="disabled")
