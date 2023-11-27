# Milestone 2
# Function to create and return a list of favorite fruits
def create_favorite_fruits_list():
    return ["Apple", "Banana", "Cherry", "Grapes", "Mango"]

# Function to randomly select a fruit from the list
def select_random_fruit(fruit_list):
    import random
    return random.choice(fruit_list)

# Function to validate user input
def validate_guess(user_input):
    if len(user_input) == 1 and user_input.isalpha():
        return "Good guess!"
    else:
        return "Oops! That is not a valid input."

# Main execution
def main():
    # Task 1: Create and print a list of favorite fruits
    favorite_fruits = create_favorite_fruits_list()
    print(favorite_fruits)

    # Task 2: Select and print a random fruit
    random_fruit = select_random_fruit(favorite_fruits)
    print(random_fruit)

    # Task 3: Ask user for input and validate
    user_guess = input("Please enter a single letter: ")
    validation_message = validate_guess(user_guess)
    print(validation_message)

# Run the main function
if __name__ == "__main__":
    main()
