# main.py
import random

# get user guess
def get_guess():
    while True:
        try:
            guess = int(input(f'Guessing number ({lower_range} ~ {upper_range}): '))
            if lower_range <= guess <= upper_range:
                return guess
            else:
                print('Invalid input, try again\n')
        except ValueError:
            print('Invalid input, please enter a valid number\n')

# validate guess
def check_guess(guess, answer):
    if guess < answer:
        return 'Too low\n'
    elif guess > answer:
        return 'Too high\n'
    else:
        return 'Correct\n'

# track attempts, detect game is over or not
def game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, answer)

        if result == 'Correct\n':
            print(f'Correct, you guessed the {answer} in {attempts} attempts')
            won = True
            break
        else:
            print(f'{result}')
    
    if not won:
        print(f'You ran out of attempts, the number is {answer}')

if __name__ == '__main__':
    print('Welcome Guess!\n')
    again = True

    while again:
        # define range and max_attempts
        lower_range = int(input('Enter the lower bound: '))
        upper_range = int(input('Enter the upper bound: '))
        print('You can attempts 5 times\n')
        max_attempts = 5

        # generate the random number
        answer = random.randint(lower_range, upper_range)

        game()

        play_again = input('Do you went to play again? (Yes / No): ')
        if play_again.lower() == 'no':
            again = False
