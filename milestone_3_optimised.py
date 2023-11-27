# Milestone 3.py

# Task 3
# Define the check_guess function
def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

# Define the ask_for_input function
def ask_for_input(secret_word):
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            if check_guess(guess, secret_word):
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main execution
secret_word = "apple"  # Example secret word
ask_for_input(secret_word)
