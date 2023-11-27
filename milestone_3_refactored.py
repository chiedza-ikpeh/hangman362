# Milestone 3.py

def is_valid_guess(guess):
    """ Check if the guess is a valid single alphabetical character """
    return len(guess) == 1 and guess.isalpha()

def format_and_check_guess(guess, word):
    """ Format the guess to lowercase and check if it is in the secret word """
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def prompt_user_for_guess():
    """ Prompt user for a letter and validate it """
    while True:
        guess = input("Guess a letter: ")
        if is_valid_guess(guess):
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def play_hangman(secret_word):
    """ Main function to play Hangman game """
    while True:
        user_guess = prompt_user_for_guess()
        if format_and_check_guess(user_guess, secret_word):
            break

# Main execution
secret_word = "apple"  # Example secret word
play_hangman(secret_word)
