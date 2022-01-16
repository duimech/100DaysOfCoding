from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# List of objects containing questions and answers
question_bank = []

# Create an object for each question containing the question and the answer
for item in question_data:
    question = Question(item["text"], item["answer"] )
    question_bank.append(question)

# Create the quiz using a list of objects 
quiz = QuizBrain(question_bank)

# Keep asking questions until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

# Show users final score
quiz.final_score()


# Procedural:
# question_bank = []

# for item in question_data:
#     question = Question(item["text"], item["answer"] )
#     question_bank.append(question)
# question_number = 0
# correct_answers = 0
# while question_number < len(question_bank):
#     user_answer = str.lower(input(f"{question_bank[question_number].text} (True/False)?:  "))
#     if user_answer.title() == question_bank[question_number].answer:
#         correct_answers += 1
#         print(f"Correct.")
#         question_number += 1
#     else:
#         print(f"Incorrect.")
#         question_number += 1

# score = int(round(correct_answers / len(question_bank) * 100))
# print(f"\nTotal questions: {len(question_bank)}")
# print(f"Total correct answers: {correct_answers}")
# print(f"Your scrore is {score}")

