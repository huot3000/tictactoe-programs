# One-Player Tic Tac Toe Game (Bot Opponent)

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

def getPlayerName():
    # Ask player name
    global player
    print('We\'re going to play tic-tac-toe!')
    time.sleep(0.5)
    print('')
    print('What\'s your name')
    player = str(input())
    print('')
    while player == '':
        print('Enter your name')
        player = str(input())
    time.sleep(0.5)
    print('')
    print('Hi, ' + player + '!')

# Randomly assign X or O

def assignXO():
    rand = random.randint(0,1)
    global turn
    if rand == 1:
        time.sleep(0.5)
        print(player + ', you\'re X. The computer is O.')
        time.sleep(0.5)
        print('')
        print('X goes first. ' + player +', you start.')
        turn = player
    else:
        time.sleep(0.5)
        print(player + ', you\'re O. The computer is X.')
        time.sleep(0.5)
        print('')
        print('The computer goes first.')
        turn = 'bot'

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
    
### Game Flow
    
# Ask player names
getPlayerName()
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
    if turn == player:
        print('Make your move, ' + str(turn) + '. Place your ' + str(letter) + ' in a case (1 to 9).')
        move = int(input()) # Ask for move
        while board[move] != ' ':  # Check if case is free
            print('You can\'t pick this one! Try again.')
            move = int(input())
        
        board[move] = letter    # Record move

    else:
        print('The bot is making a move')
        move = random.randint(1,10) # Bot picks random number between 1 and 9
        while board[move] != ' ':  # Check if case is free
            move = random.randint(1,10)

        board[move] = letter    # Record move


    if isWinner(board, letter):
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
    elif turn == player: #Switching players
        turn = 'bot'
    else:
        turn = player
    if letter == 'X':
        letter = 'O'
    else:
        letter = 'X'
        

    


