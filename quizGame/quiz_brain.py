class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.questions_list = q_bank
        self.score = 0

    # Get a question from the list of objects containing questions
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)?:  ")
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is {self.score} / {self.question_number}\n")

    # See if the answer to the question is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct.")
            self.score += 1
        else:
            print("Incorrect")


    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False


    def final_score(self):
        score_percent = int(round((self.score / self.question_number) * 100))
        print(f"You're final score is {score_percent} percent.")