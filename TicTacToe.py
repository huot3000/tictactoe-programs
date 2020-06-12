# Two-Player Tic Tac Toe Game

# Setup

import time
import random
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Drawing the board

def drawBoard():
    print('-----------')
    print(' ' +  board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('-----------')
    print(' ' +  board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-----------')
    print(' ' +  board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('-----------')

# Player setup

def assignPlayers():
    # Ask names
    global player1, player2
    print('We\'re going to play tic-tac-toe!')
    time.sleep(0.5)
    print('')
    print('This is a two player game. Get a friend!')
    time.sleep(0.5)
    print('')
    print('What is the name of the first player?')
    player1 = str(input())
    print('')
    while player1 == '':
        print('Enter a name')
        player1 = str(input())
    time.sleep(0.5)
    print('What is the name of the second player?')
    player2 = str(input())
    print('')
    while player2 == '':
        print('Enter a name')
        player2 = str(input())
    print('')
    print('Hi, ' + player1 + ' and ' + player2 +'!')

# Randomly assign X or O

def assignXO():
    rand = random.randint(0,1)
    global turn
    if rand == 1:
        time.sleep(0.5)
        print(player1 + ', you\'re X. ' + player2 + ', you\'re O.')
        time.sleep(0.5)
        print('')
        print('X goes first. ' + player1 +', you start.')
        turn = player1
    else:
        time.sleep(0.5)
        print(player1 + ', you\'re O. ' + player2 + ', you\'re X.')
        time.sleep(0.5)
        print('')
        print('X goes first. ' + player2 +', you start.')
        turn = player2

# Check if case free

def isCaseFree():
    return board[move] == ' '

# Check if winner

def isWinner(board, letter):
    return((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))
    
# If winner, announce winner

if isWinner == True:
    print(letter + ' wins!')

### Game Flow
    
# Ask player names
assignPlayers()
time.sleep(0.5)
print('')

# Randomly assign letter for players
assignXO()
time.sleep(0.5)
print('')

# Taking turns

letter = 'X'

for i in range(9):
    print('')
    drawBoard()
    print('Make your move, ' + str(turn) + '. Place your ' + str(letter) + ' in a case (1 to 9).')
    move = int(input()) # Ask for move

    while not isCaseFree():  # Check if case is free
        print('You can\'t pick this one! Try again.')
        move = int(input())
        
    board[move] = letter    # Record move

    win = isWinner(board, letter) # Check if there's a win
    if win == True:
        print('')
        drawBoard()
        print('')
        print('Congrats, ' + str(turn) +'! You won!')
        print('''  _______
 |       |
(|  TTT  |)
 | CHAMP |
  \     /
   `---'
   _|_|_''')
        print('')
        time.sleep(5)
        break
    elif turn == player1: #Switching players
        turn = player2
    else:
        turn = player1
    if letter == 'X':
        letter = 'O'
    else:
        letter = 'X'
        

    


