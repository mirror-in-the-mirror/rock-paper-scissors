import random as random
import time

cH = random.randint(0, 2)  # cH = Computer Hand

name = str(input('Please enter your name here: '))
if name == "":
    name = 'User'
print(f'Hello {name}')
time.sleep(0.7)
print('\nPlease pick a hand')
print('0: Rock\n1: Paper\n2: Scissors')


def tanganorang():
    global userHand
    userHand = str(input('Input here: '))
    if userHand == '0':
        return 'Rock'
    elif userHand == '1':
        return 'Paper'
    elif userHand == '2':
        return 'Scissors'
    else:
        print('Please enter a valid number')


to = tanganorang()
print(f'\n{name} picked {to}')

time.sleep(0.7)


def com_hand():
    if cH == 0:
        return 'Rock'
    elif cH == 1:
        return 'Paper'
    elif cH == 2:
        return 'Scissors'


bot = com_hand()
print(f'Computer picked {bot}\n')


def determiner():  # 0: Rock, 1: Paper, 2: Scissors
    if userHand == '0' and cH == 0:  # User: Rock, Computer: Rock
        print('Tied!')
    elif userHand == '0' and cH == 1:  # User: Rock, Computer: Paper
        print('Computer wins!')
    elif userHand == '0' and cH == 2:  # User: Rock, Computer: Scissors
        print('You win!\nCongratulations!')
    elif userHand == '1' and cH == 0:  # User: Paper, Computer: Rock
        print('You win!\nCongratulations!')
    elif userHand == '1' and cH == 1:  # User: Paper, Computer: Paper
        print('Tied!')
    elif userHand == '1' and cH == 2:  # User: Paper, Computer: Scissors
        print('Computer wins!')
    elif userHand == '2' and cH == 0:  # User: Scissors, Computer: Rock
        print('You win!\nCongratulations!')
    elif userHand == '2' and cH == 1:  # User: Scissors, Computer: Paper
        print('Computer wins!')
    elif userHand == '2' and cH == 2:  # User: Scissors, Computer: Scissors
        print('Tied')


determiner()
