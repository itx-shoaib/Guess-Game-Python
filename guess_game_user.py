# This is a Guess game user edition.

# Import section
import random

print('***** Welcome to the Guess game user edition ***** \n')
print('Before playing this game please guess your number and dont tell this to computer. \n')
number = int(input('Please Enter the last number of range in which you want computer to guess i.e. 10 or 20 etc : '))
def guess_user(number):
    low = 1
    high = number
    user_feedback = ''
    while user_feedback != 'c':
        if low != high:
            random_number = random.randint(low, high)
        else:
            random_number = high

        user_feedback = input(f'Is {random_number} is too high (H) , too low (L) or Correct (C)? :').lower()

        if user_feedback == 'h':
            high = high - 1
        elif user_feedback == 'l':
            low = low + 1

        print(f'Opps! the computer guessed the number, {random_number}, correctly.')

if __name__ == '__main__':
    guess_user(number)
