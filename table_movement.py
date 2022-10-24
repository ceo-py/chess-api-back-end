from chess_game_logic import *

figures_class = {
    "Pawn": Pawn,
    "Rook": Rook,
    "Knight": Knight,
    "Bishop": Bishop,
    "Queen": Queen,
    "King": King
}

colors = {
        6: "w",
        1: "b",
        7: "w",
        0: "b"

    }
BOARD_SIZE = 8


def create_new_game():
    chess_board = []

    counter = 0
    for row in range(BOARD_SIZE):
        chess_board.append([])
        for col in range(BOARD_SIZE):
            counter += 1

            if row in (6, 1):
                chess_board[row].append(Pawn(f"Pawn - {colors[row]}", colors[row], (row, col)))

            elif row not in (7, 0):
                chess_board[row].append(f"{chr(97 + col)} - {abs(row - 8)}")
                continue

            elif col in (0, 7):
                chess_board[row].append(Rook(f"Rook - {colors[row]}", colors[row], (row, col)))

            elif col in (1, 6):
                chess_board[row].append(Knight(f"Knight - {colors[row]}", colors[row], (row, col)))

            elif col in (2, 5):
                chess_board[row].append(Bishop(f"Bishop - {colors[row]}", colors[row], (row, col)))

            elif col == 3:
                chess_board[row].append(Queen(f"Queen - {colors[row]}", colors[row], (row, col)))

            elif col == 4:
                chess_board[row].append(King(f"King - {colors[row]}", colors[row], (row, col)))

    return chess_board


def current_board(board: list):
    c_table = []

    for row in range(BOARD_SIZE):
        c_table.append([])
        for col in range(BOARD_SIZE):
            figure, color = board[row][col].split(" - ")
            try:
                c_table[row].append(figures_class[figure](f"{figure} - {color}", color, (row, col)))
            except KeyError:
                c_table[row].append(f"{chr(97 + col)} - {abs(row - 8)}")
    return c_table


def save_board(board: list):
    c_table = []

    for row in range(BOARD_SIZE):
        c_table.append([])
        for col in range(BOARD_SIZE):
            try:
                c_table[row].append(board[row][col].name)
            except AttributeError:
                c_table[row].append(board[row][col])
    return c_table
