import html
import re

class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.questions_list = q_bank
        self.score = 0

    # Get a question from the list of objects containing questions
    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        question_text = html.unescape(self.current_question.text)
        self.question_number += 1
        return f"Q{self.question_number}: {question_text}"
        # user_answer = input(f"Q{self.question_number}: {question_text} (True/False)?:  ")
        # self.check_answer(user_answer, current_question.answer)
        # print(f"Your current score is {self.score} / {self.question_number}\n")


    # See if the answer to the question is correct
    def check_answer(self, user_answer):
        answer = self.current_question.answer
        if user_answer == answer:
            self.score += 1
            return True
        else:
            return False

    # def check_answer(self, user_answer, correct_answer):
    #     if user_answer.lower() == correct_answer.lower():
    #         print("Correct.")
    #         self.score += 1
    #     else:
    #         print("Incorrect")


    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False


    # def final_score(self):
    #     score_percent = int(round((self.score / self.question_number) * 100))
    #     print(f"You're final score is {score_percent} percent.")