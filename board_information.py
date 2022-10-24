import json

web_pos = {'0 0': 1, '0 1': 2, '0 2': 3, '0 3': 4, '0 4': 5, '0 5': 6, '0 6': 7, '0 7': 8, '1 0': 9, '1 1': 10,
           '1 2': 11, '1 3': 12, '1 4': 13, '1 5': 14, '1 6': 15, '1 7': 16, '2 0': 17, '2 1': 18, '2 2': 19, '2 3': 20,
           '2 4': 21, '2 5': 22, '2 6': 23, '2 7': 24, '3 0': 25, '3 1': 26, '3 2': 27, '3 3': 28, '3 4': 29, '3 5': 30,
           '3 6': 31, '3 7': 32, '4 0': 33, '4 1': 34, '4 2': 35, '4 3': 36, '4 4': 37, '4 5': 38, '4 6': 39, '4 7': 40,
           '5 0': 41, '5 1': 42, '5 2': 43, '5 3': 44, '5 4': 45, '5 5': 46, '5 6': 47, '5 7': 48, '6 0': 49, '6 1': 50,
           '6 2': 51, '6 3': 52, '6 4': 53, '6 5': 54, '6 6': 55, '6 7': 56, '7 0': 57, '7 1': 58, '7 2': 59, '7 3': 60,
           '7 4': 61, '7 5': 62, '7 6': 63, '7 7': 64}


def getting_legal_moves_ouput(symbol, matrix):
    try:
        symbol.available_moves = []
        symbol.check_right_move(matrix)
        result = []
        for a_row, a_col in symbol.available_moves:
            result.append({"position": web_pos[f"{a_row} {a_col}"], "row": a_row, "col": a_col})
        if result:
            return result
        return 0
    except AttributeError:
        return 0


def matrix_for_api(matrix: list, game_id: str):
    result = [{"game": [{"id": game_id, "isOver": False}]}, {"pieces": []}]
    for row in range(8):
        for col in range(8):
            symbol_matrix = matrix[row][col]
            if isinstance(symbol_matrix, str):
                result[1]['pieces'].append({"position": web_pos[f"{row} {col}"], "type": 0, "color": 0, "row": row, "col": col,
                               "moves": 0})

            else:
                result[1]['pieces'].append(
                    {"position": web_pos[f"{row} {col}"], "type": symbol_matrix.name.lower().split(" - ")[0],
                     "color": symbol_matrix.color, "row": row, "col": col,
                     "moves": getting_legal_moves_ouput(symbol_matrix, matrix)})

    # [print(' '.join(x if isinstance(x, str) else f"{x.name}" for x in row)) for row in
    #  matrix]
    return json.dumps(result, indent=9)


def move_try(c_row, c_col, m_row, m_col, c_board):
    try:
        target = c_board[c_row][c_col]
        target.available_moves = []
        target.check_right_move(c_board)
        if [m_row, m_col] in target.available_moves:
            target.position = (m_row, m_col)
            c_board[m_row][m_col], c_board[c_row][
                c_col] = target, f"{chr(97 + c_col)} - {abs(c_row - 8)}"
            target.row, target.col = m_row, m_col
    except AttributeError:
        pass

