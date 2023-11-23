"""
Number guessing game
Preston Rizzo
"""
# Put your import statements here
import random

# Put your named constants here
GAME_WON = "W"
GAME_LOST = "L"
MAX_GUESSES = 6


# Put function definitions here
def play_game(number):
    """
    Allows the user to play the game
    :param number: The number the user is attempting to guess
    :return: returns GAME_WON or GAME_LOST depending on results
    """
    print("Let's play a game\nguess a number between 1 and 100")
    guess = 0
    attempts = MAX_GUESSES
    count = 0
    while MAX_GUESSES > count and guess != number:
        guess = get_user_guess()
        if number == guess:
            count += 1
            attempts -= 1
            print(f"Congratulations, you guessed the number after {count} guesses!")
            return GAME_WON
        elif number > guess:
            count += 1
            attempts -= 1
            print(f"Your guess is too low! You have {attempts} guesses remaining.")
        elif number < guess:
            count += 1
            attempts -= 1
            print(f"Your guess is too high! You have {attempts} guesses remaining.")
    print(f"\nSorry, you ran out of guesses. The number was {number}.")
    return GAME_LOST


def get_user_guess():
    """
    Gets the input of the user to use in play_game
    :return: The number inputted by the user
    """
    guess = input("Put in your guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess <= 0 or guess > 100:
            guess = get_user_guess()
    else:
        guess = get_user_guess()
    return guess


def main():
    """
    This function ends when the user no longer wants to play.
    """
    replay = "Y"
    while replay == "y" or replay == "Y":
        num = random.randint(1, 100)
        play_game(num)
        replay = str(input("Do you want to play again? "))


if __name__ == "__main__":
    main()
