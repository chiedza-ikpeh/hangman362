# Task 7

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game instance.
        :param word_list: List of possible words.
        :param num_lives: Number of lives the player starts with, default is 5.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates game state.
        :param guess: The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            self._update_guessed_word(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        """
        Prompts the player to guess a letter and validates the input.
        """
        while True:
            guess = input("Guess a letter: ").lower()
            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

    def _update_guessed_word(self, guess):
        """
        Updates the guessed word with the correct guess.
        :param guess: The letter correctly guessed by the player.
        """
        letter_newly_guessed = False
        for i, letter in enumerate(self.word):
            if letter == guess and self.word_guessed[i] == '_':
                self.word_guessed[i] = guess
                letter_newly_guessed = True
        if letter_newly_guessed:
            self.num_letters -= 1

    def _handle_incorrect_guess(self, guess):
        """
        Handles the scenario where the guessed letter is not in the word.
        :param guess: The letter incorrectly guessed by the player.
        """
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_valid_guess(self, guess):
        """
        Checks if the guess is a single alphabetical character.
        :param guess: The letter guessed by the player.
        :return: True if the guess is valid, False otherwise.
        """
        return len(guess) == 1 and guess.isalpha()

# Example usage
word_list = ["apple", "banana", "cherry"]
game = Hangman(word_list)
game.ask_for_input()
