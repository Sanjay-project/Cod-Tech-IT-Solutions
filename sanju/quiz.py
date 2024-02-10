import random

# Define quiz questions, options, and correct answers
questions = [
    "What is the capital of india?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal in the world?",
]

options = [
    ["A.New delhi", "B.Gujarat", "C.Jaipur", "D. Nepal"],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Gorilla"],
]

correct_answers = ['A', 'B', 'B']

# Shuffle the order of questions
question_order = list(range(len(questions)))
random.shuffle(question_order)

# Initialize score
score = 0

# Function to display and process the quiz
def run_quiz():
    global score
    for i in question_order:
        print("\nQuestion:", questions[i])
        for option in options[i]:
            print(option)

        user_answer = input("Your answer (enter the corresponding letter): ").upper()

        if user_answer == correct_answers[i]:
            print("Correct Answer!!")
            score += 1
        else:
            print("Incorrect Answer. The correct answer is", correct_answers[i])

# Run the quiz
run_quiz()

# Display the final score
print("\n Quiz completed! Your final score:", score, "out of", len(questions))