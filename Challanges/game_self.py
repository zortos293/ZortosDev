import random
import os
player_2_repeat = True
player_1_repeat = True
a = ['.','.','.','.','.','.','.','.','.']
winner = ''

board = """
[{0}] [{1}] [{2}] 
[{3}] [{4}] [{5}] 
[{6}] [{7}] [{8}] 
"""

def check_strike():
    if (a[0] == '+' and a[3] == '+' and a[6] == '+' ) or  (a[0] == '+' and a[1] == '+' and a[2] == '+' ) or (a[0] == '+' and a[4] == '+' and a[8] == '+') or (a[6] == '+' and a[7] == '+' and a[8] == '+' ) or (a[3] == '+' and a[4] == '+' and a[5] == '+' ) or (a[2] == '+' and a[5] == '+' and a[8] == '+' ) or (a[1] == '+' and a[4] == '+' and a[7] == '+' )or (a[2] == '+' and a[4] == '+' and a[6] == '+' ):
        return 'Player 2'
    elif  (a[0] == 'x' and a[3] == 'x' and a[6] == 'x' ) or (a[0] == 'x' and a[1] == 'x' and a[2] == 'x' ) or (a[0] == 'x' and a[4] == 'x' and a[8] == 'x' ) or (a[6] == 'x' and a[7] == 'x' and a[8] == 'x' ) or (a[3] == 'x' and a[4] == 'x' and a[5] == 'x' ) or (a[2] == 'x' and a[5] == 'x' and a[8] == 'x' ) or (a[1] == 'x' and a[4] == 'x' and a[7] == 'x' )or (a[2] == 'x' and a[4] == 'x' and a[6] == 'x' ):
        return 'Player 1'
    else:
        return 'N'
os.system('cls')
while True:
    winner = check_strike()
    if  winner != 'N':
        os.system('cls')
        print(board.format(*a))
        print(f'{winner} Won the Game !!')
        break

    while player_1_repeat == True:
        print(board.format(*a))
        print(board)
        selection = int(input('Player 1 [x] Choose Number\n>>> '))
        if selection in range(0,9):
            if a[selection] != '.':
                print('Someone placed it there already try again') 
            else:
                a[selection] = 'x'
                player_1_repeat = False

    if  '.' not in a:
        os.system('cls')
        print('TIE GG!')
        break
    os.system('cls')


    while player_2_repeat == True:
        print(board.format(*a))
        print(board)
        selection = int(input('Player 2 [+] Choose Number\n>>> '))
        if selection in range(0,9):
            if a[selection] != '.':
                print('Someone placed it there already try again') 
            else:
                a[selection] = '+'
                player_2_repeat = False
        os.system('cls')

    
    player_1_repeat = True
    player_2_repeat = True

