from IPython.display import clear_output
import random
def display_board(board):
      #  board = ['x','1','2','3','4','5','6','7','8','9']
    clear_output(True)
    print('   |   |'   )
    print(f' {board[7]} | {board[8]} | {board[9]}'   )
    print('   |   |'   )
    print('-----------  ')
    print('   |   |'   )
    print(f' {board[4]} | {board[5]} | {board[6]}'  )
    print('   |   |'   )
    print('-----------  ')
    print('   |   |'   )
    print(f' {board[1]} | {board[2]} | {board[3]}'   )
    print('   |   | '  )


def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input("Player1: Choose X or O: ").upper()
        
    if marker == 'X':
        
        return ('X','O')
    else:
        return ('O','X')



def place_marker(board, marker, position):      
    board[position] = marker       


def win_check(board,mark):
    # WIN TIC TAC TOE? 
    # check all rows, and see if they all share the same marker?
    # check all columns, and see if marker matches
    # Check the two diagonals, and see if there's a match
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
        

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False           
    return True

def player_choice(player,board):
    
    position = 0
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(f'{player} please choose your next position (1-9)'))

    return position

def replay():
    answer = 'nyeaeh'
    
    while answer not in ['yes','no']:
        answer = input('do you want to play again? (yes or no)')
        
        if answer not in ['yes','no']:
            print ("invalid answer, please write yes or no")
        
    return answer == 'yes'    

# everything put together to make the game

while True:
    test_board = ['#','1','2','3','4','5','6','7','8','9']
    print ("Welcome to the game of Tic Tac Toe!")
    print ("Please note that answers are case sensitive!")
    print ("Numbers 1 to 9 correspond to the following spots")
    display_board(test_board)
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    player_1_marker, player_2_marker = player_input()
    
    turn = choose_first()
    
    print( turn + ' will go first.')
        
    play_game = input('Ready to play? yes or no:  ')
    
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
                # show the board
            display_board(board)
                # choose a position
            position = player_choice('player 1',board)    
                # place the marker on the position
            place_marker(board,player_1_marker,position)
                # check if they won
            if win_check(board,player_1_marker):
                display_board(board)
                print('Player 1 has won')
                game_on = False
                   # check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie Game!")
                    break
                 # no tie andd win? next player's turn
                else:
                    turn = 'Player 2'
                
                
                
        else:
            # show the board
            display_board(board)
                # choose a position
            position = player_choice('player 2',board)    
                # place the marker on the position
            place_marker(board,player_2_marker,position)
                # check if they won
            if win_check(board,player_2_marker):
                display_board(board)
                print('Player 2 has won')
                game_on = False
                   # check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie Game!")
                    game_on = False
                    break
                 # no tie andd win? next player's turn
                else:
                    turn = 'Player 1'
                

  

    if not replay():
        break