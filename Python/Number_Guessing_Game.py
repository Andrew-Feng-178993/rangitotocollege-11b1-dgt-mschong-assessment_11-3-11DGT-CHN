import random

def guess_number(high_number):
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
                print(f"Congratulations! You've guessed the number in {attempts + 1} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter another valid number.")
    
print("WELCOME TO ANDREW'S GUESSING GAME!!!\n")

print("Levels:")
print("Easy: 1 - 100")
print("Medium: 1 - 1000")
print("Hard: 1 - 10000")
print("Extra Hard: 1 - 100000\n")

while True:
    level = input("Pick a difficulty level: Easy, Medium, Hard, Extra Hard.\n").capitalize()
    if level == "Easy":
        guess_number(100)
    elif level == "Medium":
        guess_number(1000)
    elif level == "Hard":
        guess_number(10000)
    elif level == "Extra Hard":
        guess_number(100000)
    else:
        print("Invalid level! Please choose another level.")
        
        
    again = input("Do you want to play again?: ").lower()
    if again != 'yes':
        print("Ok, thank you for playing! :)")
        break

