import random
from art import logo


# CREATE THE BOARD
def create_board(board):
    print("  |   |")
    print("" + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("----------")
    print("  |   |")
    print("" + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("----------")
    print("  |   |")
    print("" + board[1] + ' | ' + board[2] + ' | ' + board[3])


# TAKES PLAYER INPUT AND ASSIGN MARKER
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 Do you want to be X or O? ").upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# ASSIGN MARKER TO ASSIGNED POSITION
def place_marker(board, marker, position):
    board[position] = marker


# CONDITION FOR WINNING
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark))


# RANDOMLY DECIDES WHICH PLAYER GOES FIRST
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# RETURNS WHETHER SPACE ON BOARD IS FREELY AVAILABLE
def space_check(board, position):
    return board[position] == ' '


# CHECK IF BOARD IS FULL AND RETURN BOOLEAN VALUE
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# ASKS PLAYER FOR NEXT POSITION
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your next position: (1-9) "))
    return position


# ASKS PLAYER IF THEY WANT TO PLAY AGAIN
def replay():
    return input("DO you want to play again? Enter (Y/N)").lower()


"""############## MAIN GAME ############"""
print(logo)
print("Welcome to Tic Tac Toe")

is_continue = True
while is_continue:
    """Reset the board"""
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Are you ready for a game of Tic Tac Toe? Enter (Y/N) ").lower()

    if play_game[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':  # Player 1 turn
            create_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                create_board(theBoard)
                print('Congratulations! You have won the game.')
                game_on = False
            else:
                if full_board_check(theBoard):
                    create_board(theBoard)
                    print('Game Draw')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2 turn
            create_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                create_board(theBoard)
                print('Player 2 won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    create_board(theBoard)
                    print('Game Draw')
                    break
                else:
                    turn = 'Player 1'

    if replay() == 'n':
        is_continue = False
