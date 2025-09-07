import random

guesses_num = []

easy_level_num = 100
medium_level_num = 1000
hard_level_num = 10000
extra_hard_level_num = 100000

level = input("Pick a level of difficulty: Easy, Medium, Hard, Extra Hard.\n")

if level == "Easy":
    random_num = random.randint(1, easy_level_num)
    print(random_num)
elif level == "Medium":
    random_num = random.randint(1, medium_level_num)
    print(random_num)
elif level == "Hard":
    random_num = random.randint(1, hard_level_num)
    print(random_num)
elif level == "Extra Hard":
    random_num = random.randint(1, extra_hard_level_num)
    print(random_num)
else:
    print("That is not a valid level! Please pick again.")
    level = input("Pick a level of difficulty: Easy, Medium, Hard, Extra Hard.\n")



guess = int(input("Please guess a number"))
while True:
    if guess < 1 or guess > easy_level_num:
        print("That is not within the valid range!")
    elif guess == random_num:
        list.append("lol")
        print(f"Congratulations! You guessed the number in {len(guesses_num)} guesses!")
    elif guess < random_num:
        list.append("lol")
        print("The number you are looking for is higher!")
    elif guess > random_num:
        list.append("lol")
        print("The number you are looking for is lower!")


