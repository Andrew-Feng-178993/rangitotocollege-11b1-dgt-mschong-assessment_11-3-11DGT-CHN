import random

print("WELCOME TO ANDREW'S GUESSING GAME!!!")
list = []

easy_level_num = 100
medium_level_num = 1000
hard_level_num = 10000
extra_hard_level_num = 100000

while True:
    level = input("Pick a level of difficulty: Easy, Medium, Hard, Extra Hard.\n")

    if level == "Easy":
        random_num = random.randint(1, easy_level_num)
        print(random_num)
        
        break
    elif level == "Medium":
        random_num = random.randint(1, medium_level_num)
        print(random_num)
      
        break
    elif level == "Hard":
        random_num = random.randint(1, hard_level_num)
        print(random_num)
   
        break
    elif level == "Extra Hard":
        random_num = random.randint(1, extra_hard_level_num)
        print(random_num)
   
        break
    else:
        print("That is not a valid level! Please pick again.")
   
guess = int(input("Please guess a number:\n"))
while True:
    ###if guess < 1 or guess > limit:
        ###print("That is not within the valid range!")
    if guess < random_num:
        list.append("lol")
        print("The number you are looking for is higher!")
        guess = int(input("Please guess a number:\n"))
        
    elif guess > random_num:
        list.append("lol")
        print("The number you are looking for is lower!")
        guess = int(input("Please guess a number:\n"))
        
    elif guess == random_num:
        list.append("lol")
        print(f"Congratulations! You guessed the number in {len(list)} guesses!")
        





