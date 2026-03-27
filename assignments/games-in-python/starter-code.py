# 📘 Assignment: Hangman Game Challenge
# 🎯 Objective: Build a classic word-guessing game using Python strings, loops, and user input.

import random

# List of possible words for the game
words = ['python', 'hangman', 'challenge', 'programming', 'computer']

# TODO: Task 1 - Implement Hangman Game
# Randomly select a word from the list
secret_word = random.choice(words)

# Initialize variables for game state
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6  # Standard hangman allows 6 incorrect guesses

# Main game loop
while incorrect_guesses < max_incorrect and ''.join([letter if letter in guessed_letters else '_' for letter in secret_word]) != secret_word:
    # Display current progress
    current_progress = ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])
    print(f"Current word: {current_progress}")
    print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if guess is valid (single letter, not already guessed)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is in the secret word
    if guess in secret_word:
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Incorrect guess.")

# Display win/lose message
if ''.join([letter if letter in guessed_letters else '_' for letter in secret_word]) == secret_word:
    print(f"Congratulations! You guessed the word: {secret_word}")
else:
    print(f"Sorry, you ran out of guesses. The word was: {secret_word}")
