import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Cols
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Tie"
    return None

def main():
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
            if board[move] != " ":
                print("Position already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        board[move] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
