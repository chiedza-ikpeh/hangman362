# Task 1
# Step 1: Create a list of 5 favorite fruits and 
# Step 2: assign it to a variable called word_list
word_list = ["Apple", "Banana", "Cherry", "Grapes", "Mango"]

# Step 3: Print the list
print(word_list)

# Task 2
# Step 1: Go to the first line of your file.
# Step 2: Write import random on the line
import random

# Step 3: Use random.choice method to select a random word from the word_list
# Step 4: Assign the randomly generated word to a variable called word
word = random.choice(word_list)

# Step 5: Print out the randomly chosen word
print(word)

# Task 3
# Step 1: Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# This variable 'guess' will now contain the letter input by the user

# Task 4
# Sample input for demonstration purposes
guess = "A"  # In a real scenario, this would be obtained using input()

# Step 1: Check if the input is a single letter and is alphabetical
if len(guess) == 1 and guess.isalpha():
    # Step 2: Print a message for a valid guess
    message = "Good guess!"
else:
    # Step 3: Print a message for an invalid guess
    message = "Oops! That is not a valid input."

print(message)

