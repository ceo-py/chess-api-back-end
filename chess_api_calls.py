from data_base import *
from table_movement import *
from board_information import *
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import datetime
import hashlib


app = Flask(__name__)
CORS(app)
load_dotenv()
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)  # define the life span of the token


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


@app.route("/api/v1/login", methods=["POST"])
def login():
    login_details = request.get_json()
    user_from_db = users_collection.find_one({'email': login_details['email']})

    if user_from_db:
        encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
        if encrpted_password == user_from_db['password']:
            del user_from_db['_id'], user_from_db['password']
            access_token = create_access_token(identity=user_from_db['email'])
            return jsonify(access_token=access_token), 200

    return jsonify({'msg': 'The username or password is incorrect'}), 401


@app.route("/api/v1/users", methods=["POST"])
def register():
    new_user = request.get_json()
    new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest()
    doc = users_collection.find_one({"email": new_user["email"]})
    if not doc:
        users_collection.insert_one(new_user)
        return jsonify({'msg': 'User created successfully'}), 201

    return jsonify({'msg': 'email already exists'}), 409


@app.route("/api/v1/user", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user_from_db = users_collection.find_one({'email': current_user})
    if user_from_db:
        del user_from_db['_id'], user_from_db['password']
        return jsonify({'profile': user_from_db}), 200

    return jsonify({'msg': 'Profile not found'}), 404


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=7777, ssl_context='adhoc')
    app.run(host='0.0.0.0', port=7777)