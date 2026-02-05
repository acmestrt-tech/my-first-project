import random
import time

# Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# 1. Functions (Leaderboard Logic)
def get_leaderboard():
    try:
        with open("highscore.txt", "r") as f:
            scores = [int(line.strip()) for line in f.readlines()]
            return sorted(scores, reverse=True)[:3]
    except:
        return [0, 0, 0]

def save_leaderboard(scores):
    with open("highscore.txt", "w") as f:
        for s in scores:
            f.write(f"{s}\n")

# 2. Setup
leaderboard = get_leaderboard()
score = 0
lives = 3
time_limit = 5

print(f"{CYAN}🏆 --- MATH TURBO: LEADERBOARD EDITION --- 🏆{RESET}")
print(f"Top Record: {leaderboard[0]}")
print("Choose Difficulty: (1) Easy (2) Medium (3) Hard")
choice = input("> ")

if choice == "3":
    base_diff, scale = 100, 100
elif choice == "2":
    base_diff, scale = 50, 50
else:
    base_diff, scale = 20, 20

# 3. The Loop
while lives > 0:
    level = (score // 5) + 1
    difficulty = base_diff + (score // 5 * scale) 
    current_timer = max(1.5, time_limit - (score // 5 * 0.5))
    
    num1 = random.randint(1, difficulty)
    num2 = random.randint(1, difficulty)
    correct_answer = num1 + num2

    print(f"\n{YELLOW}--- Level {level} | ❤️ Lives: {lives} | ⏱️ Limit: {current_timer:.1f}s ---{RESET}")
    
    start_time = time.time()
    user_input = input(f"What is {num1} + {num2}? ")
    time_taken = time.time() - start_time

    if user_input.strip().lower() == 'exit':
        break

    try:
        user_val = int(user_input)
        if time_taken > current_timer:
            lives -= 1
            print(f"{RED}⏰ TOO SLOW! Limit was {current_timer:.1f}s.{RESET}")
        elif user_val == correct_answer:
            score += 1
            print(f"{GREEN}✨ Correct! ({time_taken:.1f}s) Score: {score}{RESET}")
        else:
            lives -= 1
            print(f"{RED}💀 Wrong! The answer was {correct_answer}.{RESET}")
    except ValueError:
        print(f"{YELLOW}❌ Invalid input! Type a number.{RESET}")

# 4. Save and Exit (Final Leaderboard Update)
leaderboard.append(score)
leaderboard = sorted(leaderboard, reverse=True)[:3]
save_leaderboard(leaderboard)

print(f"\n{CYAN}🏆 --- TOP 3 SCORES --- 🏆{RESET}")
for i, s in enumerate(leaderboard):
    print(f"{i+1}. {s}")

print(f"\n{YELLOW}Final Score: {score}. Come back soon!{RESET}")

