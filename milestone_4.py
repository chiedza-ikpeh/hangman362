# Milestone_4

import random

# Task 1
class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialize attributes
        self.word = random.choice(word_list)  # Pick a random word from word_list
        self.word_guessed = ['_' for _ in self.word]  # Initialize word_guessed with underscores
        self.num_letters = len(set(self.word))  # Count of unique letters in the word
        self.num_lives = num_lives  # Number of lives the player has
        self.word_list = word_list  # Store the list of words
        self.list_of_guesses = []  # Initialize an empty list for guesses

# Example usage
word_list = ["apple", "banana", "cherry"]  # Example word list
game = Hangman(word_list)

# Printing attributes to verify initialization
print("Word:", game.word)
print("Word Guessed:", game.word_guessed)
print("Number of Unique Letters:", game.num_letters)
print("Number of Lives:", game.num_lives)
print("List of Guesses:", game.list_of_guesses)

# Task 2
class Hangman:
    # ... (previous code for __init__, ask_for_input)
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Loop through each letter in the word
            for i, letter in enumerate(self.word):
                # Check if the letter is equal to the guess
                if letter == guess:
                    # Replace the corresponding "_" in word_guessed with the guess
                    self.word_guessed[i] = guess

            # Reduce num_letters by 1 only if this is a new letter
            if self.word_guessed.count(guess) == 1:
                self.num_letters -= 1
        # Additional logic for incorrect guess will be implemented in future tasks

# Task 3
class Hangman:
    # ... (previous code for __init__, ask_for_input)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Variable to track if the letter was newly guessed
            letter_newly_guessed = False
            
            # Loop through each letter in the word
            for i, letter in enumerate(self.word):
                # Check if the letter is equal to the guess
                if letter == guess:
                    # Replace the corresponding "_" in word_guessed with the guess
                    if self.word_guessed[i] == '_':
                        letter_newly_guessed = True
                    self.word_guessed[i] = guess

            # Reduce num_letters by 1 if the letter was newly guessed
            if letter_newly_guessed:
                self.num_letters -= 1
        # Additional logic for incorrect guess will be implemented in future tasks

# Task 4
class Hangman:
    # ... (previous code for __init__, ask_for_input)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            # (existing code for handling correct guess)
        else:
            # Step 1: Else statement for handling incorrect guess
            self.num_lives -= 1  # Step 2: Reduce num_lives by 1

            # Step 3: Print messages
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            # Additional handling for when num_lives reaches 0 can be added later

