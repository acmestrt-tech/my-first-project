
import random

# 1. Functions (Tools)
def get_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(new_score):
    with open("highscore.txt", "w") as f:
        f.write(str(new_score))

# 2. Setup (Ingredients)
high_score = get_high_score()
score = 0
lives = 3

# 3. The Game Loop (The Cooking)
while lives > 0:
    level = (score // 5) + 1
    difficulty = 50 + (score // 5 * 50) 
    
    num1 = random.randint(1, difficulty)
    num2 = random.randint(1, difficulty)
    correct_answer = num1 + num2

    print(f"\n--- Level {level} | ❤️ Lives: {lives} | Record: {high_score} ---")
    user_input = input(f"What is {num1} + {num2}? (or 'exit'): ")

    if user_input.lower() == 'exit':
        break

    try:
        if int(user_input) == correct_answer:
            score += 1
            print(f"✨ Correct! Score: {score}")
        else:
            lives -= 1
            if lives > 0:
                print(f"💀 Wrong! The answer was {correct_answer}.")
            else:
                print(f"💥 GAME OVER! The answer was {correct_answer}.")
    except ValueError:
        print("❌ Invalid input! Type a number.")

# 4. Wrap Up (Serving)
if score > high_score:
    print(f"\n🏆 NEW RECORD: {score}!")
    save_high_score(score)
else:
    print(f"\nFinal Score: {score}")

