"""My wordle game."""

import random

EASY_WORDS = [
    "lamp", "tree", "game", "fish", "book", "frog", "milk", "star", "sand", "fire"
]

MEDIUM_WORDS = [
    "apple", "crane", "doubt", "flood", "giant", "haste", "joker", "lemon", "mango", "ocean"
]

HARD_WORDS = [
    "planet", "stream", "flight", "silver", "castle", "donkey", "hunter", "object", "puzzle", "rocket"
]

EXTRA_HARD_WORDS = [
    "bananas", "journey", "picture", "silence", "villain", "zephyrs", "crystal", "freedom", "library", "penguin"
]

# keep top scores separately for each level
scores = {
    "Easy": [],
    "Medium": [],
    "Hard": [],
    "Extra Hard": []
}


def pick_secret_word(word_list):
    return random.choice(word_list)


def get_feedback(guess, secret):
    feedback = []
    secret_chars = list(secret)

    for i, ch in enumerate(guess):
        if ch == secret[i]:
            feedback.append("🟩")
            secret_chars[i] = None
        else:
            feedback.append(None)

    for i, ch in enumerate(guess):
        if feedback[i] is None:
            if ch in secret_chars:
                feedback[i] = "🟨"
                secret_chars[secret_chars.index(ch)] = None
            else:
                feedback[i] = "🟥"

    return "".join(feedback)


def is_valid_guess(guess, word_length):
    return len(guess) == word_length and guess.isalpha()


def play_wordle(word_list, word_length, level_name):
    secret = pick_secret_word(word_list)
    MAX_GUESSES = 6
    guesses = 0

    print(f"\nWELCOME TO ANDREW'S WORDLE ({level_name.upper()})!!!\n")
    print(f"Guess the {word_length}-letter word. You have {MAX_GUESSES} tries.\n")

    while guesses < MAX_GUESSES:
        guess = input(f"Guess {guesses + 1}/{MAX_GUESSES}: ").lower().strip()

        if not is_valid_guess(guess, word_length):
            print(f"Invalid guess. Must be {word_length} letters and only contain letters.\n")
            continue

        feedback = get_feedback(guess, secret)
        print(feedback + "\n")

        guesses += 1

        if guess == secret:
            print(f"🎉 YOU GOT IT! NICE JOB!!! It took you {guesses} guesses.\n")

            # store score in the correct level and keep top 3
            scores[level_name].append(guesses)
            scores[level_name].sort()
            scores[level_name] = scores[level_name][:3]

            # print leaderboard
            print(f"🏆 Top Scores for {level_name} 🏆")
            for i, score in enumerate(scores[level_name], 1):
                print(f"{i}. {score} guesses")
            print()
            return

    # if user fails
    print(f"😭 You ran out of guesses! The word was: {secret}\n")


print("WELCOME TO ANDREW'S WORDLE!!!\n")
print("Levels:")
print("Easy: 4-letter words")
print("Medium: 5-letter words")
print("Hard: 6-letter words")
print("Extra Hard: 7-letter words\n")

while True:
    level = input("Pick a difficulty level: Easy, Medium, Hard, Extra Hard.\n").capitalize()

    if level == "Easy":
        play_wordle(EASY_WORDS, 4, "Easy")
    elif level == "Medium":
        play_wordle(MEDIUM_WORDS, 5, "Medium")
    elif level == "Hard":
        play_wordle(HARD_WORDS, 6, "Hard")
    elif level == "Extra hard":  
        play_wordle(EXTRA_HARD_WORDS, 7, "Extra Hard")
    else:
        print("Invalid level! Please choose another level.\n")
        continue

    again = input("Do you want to play again?: ").lower()
    if again != 'yes':
        print("Ok, thank you for playing Wordle! :)")
        break
