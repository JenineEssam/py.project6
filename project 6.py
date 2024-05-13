import random


def guess_the_letter():
    # Generate a random letter
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    secret_letter = random.choice(alphabet)

    print("Welcome to the Guess the Letter game!")
    print("I've picked a random letter from A to Z. Can you guess it?")

    attempts = 0

    while True:
        guess = input("Enter your guess (a single letter): ").lower()
        attempts += 1

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the guess is correct
        if guess == secret_letter:
            print(f"Congratulations! You've guessed the letter '{secret_letter}' correctly in {attempts} attempts!")
            break
        else:
            print("Incorrect! Try again.")


# Run the game
guess_the_letter()
