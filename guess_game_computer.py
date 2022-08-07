#This is a Guess game computer edition.

#Import section
import random

#main code
print('***** Welcome to the Guess game computer edition *****')
number = int(input('Enter the Limit of number: '))

def guess_computer(number):
    '''Guess number is beginner level guessing game in which we learn about
    random module.Please import random module to use it properly.'''
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess_user = int(input(f'Please Enter your guess between 1 to {number}: '))
        if guess_user > random_number:
            print(f'Hint: The number you are guessing is smaller than {guess_user}')
        elif guess_user < random_number:
            print(f'Hint: The number you are guessing is greater than {guess_user}')
        else:
            print(f'Congratulations! Your guess is right one {guess_user}')
            break

if __name__ == '__main__':
    guess_computer(number)