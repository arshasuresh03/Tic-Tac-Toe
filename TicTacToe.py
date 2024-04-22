import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def is_winner(board, player):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def is_board_full(board):
    return all(pos != ' ' for pos in board[1:])

def player_move(board):
    while True:
        move = input("Please select a position to place 'X' (1-9): ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9 and board[move] == ' ':
                return move
        print("Invalid move. Please try again.")

def computer_move(board):
    possible_moves = [pos for pos, value in enumerate(board) if value == ' ' and pos != 0]
    for player in ('O', 'X'):
        for move in possible_moves:
            board_copy = board[:]
            board_copy[move] = player
            if is_winner(board_copy, player):
                return move
    return random.choice(possible_moves)

def start_game():
    board = [' '] * 10
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_board_full(board):
        # Player's move
        player_pos = player_move(board)
        board[player_pos] = 'X'
        clear_screen()
        print_board(board)
        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            return

        # Computer's move
        computer_pos = computer_move(board)
        board[computer_pos] = 'O'
        clear_screen()
        print_board(board)
        if is_winner(board, 'O'):
            print("Sorry, you lose!")
            return

    print("It's a tie!")

def main():
    while True:
        start_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
