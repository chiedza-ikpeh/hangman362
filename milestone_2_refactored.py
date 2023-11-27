#Task 1
import random

# Function to randomly select a fruit from a predefined list
def select_random_fruit():
    favorite_fruits = ["Apple", "Banana", "Cherry", "Grapes", "Mango"]
    return random.choice(favorite_fruits)

# Function to validate user input for a single alphabetic character
def is_valid_guess(user_input):
    return "Good guess!" if len(user_input) == 1 and user_input.isalpha() else "Oops! That is not a valid input."

def main():
    print("Favorite fruits: ['Apple', 'Banana', 'Cherry', 'Grapes', 'Mango']")

    random_fruit = select_random_fruit()
    print(f"Randomly selected fruit: {random_fruit}")

    user_guess = input("Please enter a single letter: ")
    validation_message = is_valid_guess(user_guess)
    print(validation_message)

if __name__ == "__main__":
    main()
