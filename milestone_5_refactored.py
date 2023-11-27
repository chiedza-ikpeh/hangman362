def start_hangman_game(word_list):
    """
    Initiates and controls the flow of the Hangman game.
    :param word_list: List of words to be used in the game.
    """
    initial_lives = 5
    hangman_game = Hangman(word_list, initial_lives)

    while True:
        if _is_game_lost(hangman_game):
            _announce_game_loss(hangman_game.word)
            break

        if _continue_game(hangman_game):
            hangman_game.ask_for_input()
        else:
            _announce_game_win()
            break

def _is_game_lost(game):
    """
    Checks if the game is lost.
    :param game: The Hangman game instance.
    :return: True if the game is lost, otherwise False.
    """
    return game.num_lives == 0

def _announce_game_loss(correct_word):
    """
    Announces that the player has lost the game.
    :param correct_word: The correct word that was to be guessed.
    """
    print('You lost!')
    print(f"The word was: {correct_word}")

def _continue_game(game):
    """
    Determines if the game should continue.
    :param game: The Hangman game instance.
    :return: True if the game should continue, otherwise False.
    """
    return game.num_letters > 0

def _announce_game_win():
    """
    Announces that the player has won the game.
    """
    print('Congratulations. You won the game!')

# Example usage
word_list = ["apple", "banana", "cherry"]
start_hangman_game(word_list)
