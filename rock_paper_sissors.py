import random

options = ['Rock', 'Paper', 'Scissors']
player = input('Whats your Name? ')
player = player.capitalize()


#decide who wins
def check_win():
    #rock beats sissors
    if choice == 'Rock' and computer == 'Scissors':
        print('Rock breaks Scissors,', player, 'is the winner!!')
        print('Choose again, or ^ to exit.')
        print()
    #paper beats rock
    elif choice == 'Paper' and computer == 'Rock':
        print('Paper covers Rock,', player, 'is the winner!!')
        print('Choose again, or ^ to exit.')
        print()
    #sissors beat paper
    elif choice == 'Scissors' and computer == 'Paper':
        print('Scissors cut Paper,', player, 'is the winner!!')
        print('Choose again, or ^ to exit.')
        print()
    #check for draw
    elif choice == computer:
        print('DRAW!')
        print('Choose again, or ^ to exit.')
        print()
    #if not win then loss
    else:
        print('Sorry,', player, 'you loose!')
        print('Choose again, or ^ to exit.')
        print()
while True:
    #have the computer pick a play at random
    computer = random.choice(options)
    #choose what to play
    choice = input('Choose Rock, Paper, or Scissors: ')
    #validate user input
    choice = choice.lower()
    if choice.startswith('r'):
        choice = 'Rock'
        print(computer)
        check_win()

    elif choice.startswith('p'):
        choice = 'Paper'
        print(computer)
        check_win()

    elif choice.startswith('s'):
        choice = 'Scissors'
        print(computer)
        check_win()

    else:
        break
