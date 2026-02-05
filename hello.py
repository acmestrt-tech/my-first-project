# A simple math quiz
print("--- Welcome to the Termux Math Challenge ---")
num1 = 15
num2 = 27
correct_answer = num1 + num2

user_guess = int(input(f"What is {num1} + {num2}? "))

if user_guess == correct_answer:
    print("✅ Correct! You are a Python pro.")
else:
    print(f"❌ Not quite. The answer was {correct_answer}.")
