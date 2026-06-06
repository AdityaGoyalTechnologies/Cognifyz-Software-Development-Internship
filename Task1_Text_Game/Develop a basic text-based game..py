# Welcome to the Python Beginner Quiz Game!

# Display a welcome message and explain the rules
print("========================================")
print("  Welcome to the Python Beginner Quiz!  ")
print("========================================")
print("Rules:")
print("- You will be asked 3 questions about Python.")
print("- Type your answer and press Enter.")
print("- Try to get the highest score possible!\n")

# Variable to keep track of the player's score
score = 0

# --- Question 1: Simple String Matching ---
print("Question 1: What is the output of 2 ** 3 in Python?")
# Accept user input, convert to lowercase, and remove extra spaces
answer1 = input("Your answer: ").strip().lower()

if answer1 == "8":
    print("Correct! Excellent job.\n")
    score += 1  # Increase score by 1
else:
    print("Incorrect. The correct answer is 8. '**' is the exponentiation operator.\n")


# --- Question 2: Multiple Choice using if, elif, and else ---
print("Question 2: Which keyword is used to define a function in Python?")
print("(a) func")
print("(b) define")
print("(c) def")
answer2 = input("Your choice (a, b, or c): ").strip().lower()

if answer2 == "c" or answer2 == "def":
    print("Correct! 'def' is used to create a function.\n")
    score += 1
elif answer2 == "a" or answer2 == "b" or answer2 == "func" or answer2 == "define":
    print("Incorrect. The correct answer is (c) def.\n")
else:
    print("Invalid input! You didn't choose a valid option, so it counts as incorrect. The answer is (c).\n")


# --- Question 3: True/False ---
print("Question 3: True or False - Python is a compiled language.")
answer3 = input("Your answer: ").strip().lower()

if answer3 == "false" or answer3 == "f":
    print("Correct! Python is an interpreted language.\n")
    score += 1
elif answer3 == "true" or answer3 == "t":
    print("Incorrect. Python is primarily an interpreted language, not a compiled one.\n")
else:
    print("I didn't understand that input, but the correct answer was False.\n")


# --- Final Result ---
print("========================================")
print("              GAME OVER                 ")
print("========================================")

# Use conditional statements to give tailored feedback based on the final score
if score == 3:
    print("Final Score: 3/3. Perfect! You are a Python pro!")
elif score == 2:
    print("Final Score: 2/3. Good job! Just one mistake.")
elif score == 1:
    print("Final Score: 1/3. Keep studying, you'll get it next time!")
else:
    print("Final Score: 0/3. Don't give up! Review your Python basics and try again.")