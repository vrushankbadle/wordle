
import os

import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)


def color_letters(word, guess):
    '''

    word : str
        The word to guessed

    guess :  str
        The guess entered by player

    returns : str
        A string same as guess,
        letters colored green if they correspond to letters in word
        letters colored yellow if they are present in word, but index are different

    '''
    guess_list = [i for i in guess]

    guess_indices = [i for i in enumerate(guess)]

    # for letter and its index in word
    for word_idx, word_val in enumerate(word):

        # for letter and its index in guess indices
        for guess_idx, guess_val in guess_indices:

            # if letter in word and guess
            if word_val == guess_val:

                # if index of letter is same in word and guess
                if word_idx == guess_idx:

                    # color letter green
                    guess_list[guess_idx] = f'{Back.GREEN}{guess_val}{Back.RESET}'

                    # remove it from guess indices and break, so it is not colored again
                    guess_indices.remove((guess_idx, guess_val))

                    break

                # if index of letter is not same in word and guess
                else:

                    # color letter yellow
                    guess_list[guess_idx] = f'{Back.YELLOW}{guess_val}{Back.RESET}'

                    # remove it from guess indices and break, so it is not colored again
                    guess_indices.remove((guess_idx, guess_val))

                    break

    guess = ' '.join(guess_list)

    return (guess)


def game_over(word, guess):
    '''

    word : str
        The word to be guessed
    guess : str
        The guess entered by player

    returns : bool
        True if guess is same as word, False otherwise

    '''
    if guess == word:
        return True
    else:
        return False


def play_again():
    '''

    Asks player 'Play Again ?' until they press y or n,
    If input is y, the game restarts, else game ends

    '''
    global replay
    reply = None

    while reply != 'y' and reply != 'n':
        reply = input("\nPlay Again ? y/n : ")

    if reply == "y":
        replay = True
    else:
        replay = False


# Main Body ----------------------


replay = True

while replay:

    victory = False

    # main word to be guessed
    word = input("\nEnter a word : ")
    clue = input("\nEnter a clue : ")

    # clear system
    os.system('cls')

    chances = 1

    # print length of word and number of attempts
    print(f"\n You have to guess a {len(word)} letter word, in 6 attempts")
    print(f"\nClue : {clue}")

    while chances <= 6:

        # input guess from user
        guess = input(f"\n{chances} : ")

        chances += 1

        # return colored guess as per conditions
        print(color_letters(word, guess))

        # execute game_over function
        if game_over(word, guess) == True:

            # if game_over returns True, victory is True, else default victory is False
            victory = True
            break

    # if guess equal to word
    if victory:
        print("\nYOU WON !")

    # if guess not equal to word
    else:
        print(f"\nYOU LOST ! The word was {word}")

    # execute play again function
    play_again()