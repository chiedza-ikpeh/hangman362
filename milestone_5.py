# Task 1

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            print(f"The word was: {game.word}")
            break

        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

# Example usage
word_list = ["apple", "banana", "cherry"]
play_game(word_list)
