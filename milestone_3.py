# Milestone_3.py
#Task 1

while True:
    # Step 2: Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Step 3 & 4: Check if the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # If the guess is valid, break out of the loop
        break
    else:
        # Step 5: If the guess is invalid, print a message
        print("Invalid letter. Please, enter a single alphabetical character.")

#Task 2
# Assuming you have a variable 'secret_word' containing the randomly chosen word

secret_word = "apple"  # Example secret word

while True:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Check if the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good guess! {guess} is in the word.")
            break  # Assuming you want to stop the loop after a correct guess
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
