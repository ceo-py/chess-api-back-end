# chess-api-back-end

Little chess project that we work on this is backend side on the game chess. With api calls you can create and move figures.

To create a new game make a POST REQUEST - https://chess-api-test.herokuapp.com/games, it will return a new game status in JSON format
To move a figure make a PUT REQUEST - https://chess-api-test.herokuapp.com/figure/move with body json in format ```    {
        "current pos": [4,1],
        "target pos": [3,0],
        "game id": "634ecfc4d6cae51c9bc450ad"
    }``` current pos - is the figure you try to move index 0 in the list represend the row index 1 is the column index 0. Target pos goes the same
    as possitions but thats the place where you want to move the figure. Game id you will find it in the first request when you create the game.
After you make a move legal/illigal it will return current table in json format.


With GET REQUEST at any time you can simple see the current game - https://chess-api-test.herokuapp.com return a json with information
