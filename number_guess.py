import random

print('Welcome to the Computer number guesssing game.') 
answer = input('Would you like to play? (y/n): ')
if answer == 'n':
    quit
if answer == 'y':
    print("Great, Let\'s begin guessing the number.")
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Wrong. Number too low, try again.')
        elif guess > random_number: 
            print('Wrong, number too high. Try again.')
    print(f"Nice, you guessed the number {random_number} correctly.")
    print("You WIN!")
guess(20)
