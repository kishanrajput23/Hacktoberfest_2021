# Tic Tak Toe Game for 2 Players


#!/bin/python3

import random


def display_board(board):
    count = 0
    count_hor = 0

    for i in range(1, len(board) + 1, 3):
        if count < 3:
            print('   |   |   \t\t\t\t   |   |   ')
            print(f' {i} | {i+1} | {i+2} \t\t\t\t' + ' ' + board[i] + ' | ' + board[i + 1] + ' | ' + board[i + 2])
            print('   |   |   \t\t\t\t   |   |   ')
            if count_hor < 2:
                print('-----------\t\t\t\t-----------')
                count_hor += 1
            count += 1


def player_input(p):
    choice = ''

    while choice != 'X' and choice != 'O':
        choice = input(f"{p} -> Enter 'X' or 'O' : ").upper()

    if choice == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, pos):
    board[pos] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))    # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, pos):
    return board[pos] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    pos = 0

    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        pos = int(input('Choose your next position: (1-9) '))

    return pos


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


if __name__ == '__main__':
    print('\n********  Welcome to Tic Tac Toe!  ********\n')
    p1 = input('PLAYER 1, Enter your Name : ').title()
    p2 = input('PLAYER 2, Enter your Name : ').title()

    while True:
        # Reset the board
        theBoard = [' '] * 10
        print()
        player1_marker, player2_marker = player_input(p1)
        turn = choose_first()
        if(turn == 'Player 1'):
            p = p1
        else:
            p = p2
        print()
        print(p + ' will go first.')

        play_game = input('\nAre you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print(f'\nCongratulations! {p1}, You have won the game!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print(f'\nCongratulations! {p2}, You have won the game!\n')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('\nThe game is a draw!\n')
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            print('\nThank You for Playing! Have a nice day...')
            break
