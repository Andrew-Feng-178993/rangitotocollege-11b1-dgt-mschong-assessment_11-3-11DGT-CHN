"""My number guessing game."""

import random

# Keep top scores separately for each difficulty
scores = {
    "Easy": [],
    "Medium": [],
    "Hard": [],
    "Extra Hard": []
}

def guess_number(high_number, level_name):
    target = random.randint(1, high_number)
    attempts = 0
    
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {high_number}: "))
            if guess < 1 or guess > high_number:
                print(f"Please enter a number between 1 and {high_number}.")
                continue
            if guess < target:
                attempts += 1
                print("Too low! Try again.")
            elif guess > target:
                attempts += 1
                print("Too high! Try again.")
            else:
                attempts += 1
                print(f"🎉 Congratulations! You've guessed the number in {attempts} attempts. 🎉\n")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # store score in the correct level
    scores[level_name].append(attempts)
    scores[level_name].sort()
    scores[level_name] = scores[level_name][:3]  # keep only top 3
    
    # print leaderboard for that level
    print(f"🏆 Top 3 Scores for Level: {level_name} 🏆")
    for i, score in enumerate(scores[level_name], 1):
        print(f"{i}. {score} attempts")
    print()

print("WELCOME TO ANDREW'S GUESSING GAME!!!\n")

print("Levels:")
print("Easy: 1 - 100")
print("Medium: 1 - 1000")
print("Hard: 1 - 10000")
print("Extra Hard: 1 - 100000\n")

while True:
    level = input("Pick a difficulty level: Easy, Medium, Hard, Extra Hard.\n").capitalize()
    if level == "Easy":
        guess_number(100, "Easy")
    elif level == "Medium":
        guess_number(1000, "Medium")
    elif level == "Hard":
        guess_number(10000, "Hard")
    elif level == "Extra hard":  # careful: capitalize() makes it "Extra hard"
        guess_number(100000, "Extra Hard")
    else:
        print("Invalid level! Please choose another level.")
        continue  # go back to asking for level
        
    again = input("Do you want to play again?: ").lower()
    if again != 'yes':
        print("Ok, thank you for playing! :)")
        break
