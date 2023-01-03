#importing the random module and setting up the winner variabl

import random

winner = ''

#computer randomly chooses rock, paper or scissors by mapping a random integer 0-2 to one of those choices 

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

#getting the user's choice with an input statement

user_choice = ''
while (user_choice != 'rock' and
        user_choice != 'paper' and
        user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

#game logic to check if computer won or not and changing the winner variable accordingly

if computer_choice == user_choice:
    winner = 'tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'computer'
else:
    winner = 'user'

#announces the result whether a tie, computer or user

if winner == 'tie':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The Computer chose', computer_choice + '.')