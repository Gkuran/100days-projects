from question_model import *;
from quiz_brain import QuizBrain;
from question_model import *
from data import *


question_bank = []

for question in question_data:
    question_text = question["text"];
    question_answer = question["answer"] 
    new_question = Question(question_text, question_answer);
    question_bank.append(new_question);
    
quiz = QuizBrain(question_bank);

while quiz.still_has_questions() == True:
    quiz.next_question();

print("You've completed the quiz!");
print(f"Your final score is: {quiz.score}/{quiz.question_number}");