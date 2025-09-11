#this is supposed to be wordle lmao

import random

# You can expand this word list or load from a file
WORD_LIST = ["apple", "banjo", "crane", "doubt", "eagle", "flood", "giant", "haste", "ivory", "joker"]

MAX_GUESSES = 6
WORD_LENGTH = 5

def pick_secret_word():
    return random.choice(WORD_LIST)

def get_feedback(guess: str, secret: str) -> str:


    feedback = []
    secret_chars = list(secret)

    # First pass: greens
    for i, ch in enumerate(guess):
        if ch == secret[i]:
            feedback.append("🟢")
            secret_chars[i] = None  # mark matched
        else:
            feedback.append(None)

    # Second pass: yellows or grays
    for i, ch in enumerate(guess):
        if feedback[i] is None:
            if ch in secret_chars:
                feedback[i] = "🟡"
                # remove one occurrence
                secret_chars[secret_chars.index(ch)] = None
            else:
                feedback[i] = "🔴"

    return "".join(feedback)

def is_valid_guess(guess: str):
    return len(guess) == WORD_LENGTH and guess.isalpha()

def wordle():
    secret = pick_secret_word()
    # Uncomment this line if you want to display the secret for debugging:
    # print(f"(Secret word is: {secret})")

    print(f"Welcome to Andrew's Wordle! Guess the {WORD_LENGTH}-letter word. You have {MAX_GUESSES} tries.\n")

    guesses = 0
    while guesses < MAX_GUESSES:
        guess = input(f"Guess {guesses + 1}/{MAX_GUESSES}: ").lower().strip()
        if not is_valid_guess(guess):
            print(f"Invalid guess. Must be {WORD_LENGTH} letters and alphabetic.")
            continue

        feedback = get_feedback(guess, secret)
        print(feedback)

        if guess == secret:
            print("Congratulations! You’ve guessed it!")
            return

        guesses += 1

    print(f"Sorry, you’ve run out of guesses. The word was: {secret}")

if __name__ == "__main__":
    wordle()

