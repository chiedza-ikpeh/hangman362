# Milestone_4
# Task
import random

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
