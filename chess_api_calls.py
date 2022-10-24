from flask import *
from data_base import *
from table_movement import *
from board_information import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


'''
id na igrite da 
end point /games        - POST(create), GET(Read)
end point /games/{id}   - GET, PUT(update), DELETE

634ec812dc1f8594e91d3ff1
imena na igrachi v bodito eventualno za suzdavane

'''


@app.route("/games", methods=["POST"])
def main_game():

    new_game = create_new_game()
    game_id = db_.create_game(save_board(new_game))
    return matrix_for_api(new_game, game_id)


@app.route("/", methods=["GET"])
def show_board():
    game_id = request.get_json()['game id']
    return matrix_for_api(current_board(db_.get_game(game_id)), game_id)


@app.route("/figure/move", methods=["PUT"])
def json_req():
    '''
    [{'current pos': [1, 0], 'target pos': [2, 0]}]

    :return:
    {'current pos': [0, 6], 'target pos': [0, 5]}
    '''
    data = request.get_json()
    print("called figure", data)
    c_row, c_col = data['current pos']
    m_row, m_col = data['target pos']
    game_id = data["game id"]
    c_board = current_board(db_.get_game(game_id))
    move_try(c_row, c_col, m_row, m_col, c_board)
    data_board = save_board(c_board)
    db_.update_game(game_id, data_board)
    [print(*row) for row in data_board]

    return matrix_for_api(c_board, game_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777)
