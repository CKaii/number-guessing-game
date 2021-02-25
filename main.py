# Number Guessing Game
import random
from art import logo

print(logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
difficulty = input('Choose a difficulty. type \'easy\' or \'hard\': ')
number = random.randrange(1, 101)
print(number)


def number_guess():

    # Two different difficulty levels (10 guesses in easy mode, only 5 guesses in hard mode).
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print('That was not an option. Goodbye.')
        return

    # Allow the player to submit a guess for a number between 1 and 100.
    guess = int(input('Make a guess: '))

    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    while attempts > 0:
        if guess == number:
            print(f'You got it! The answer is {number}.')
            return
        elif attempts == 1:
            print(
                f'You have 0 attempts remaining! The correct number is {number}')
            return
        elif guess > number:
            print('Too high.')
            attempts -= 1
            print(
                f'You have {attempts} attempts remaining to guess the number')
            guess = int(input('Make a guess: '))
        elif guess < number:
            print('Too low.')
            attempts -= 1
            print(
                f'You have {attempts} attempts remaining to guess the number')
            guess = int(input('Make a guess: '))
        else:
            print('That is not a number. Goodbye')
            return


number_guess()
