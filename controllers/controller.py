from flask import render_template
from app import app
from models.players import *
from models.player_list import *
from models.game import *


# @app.route('/')
# def index():
    # return "Shall We Play A Little Game.."


@app.route('/')
def base():
    game = Game()
    return render_template('base.html', title="Let's Scissor")

# @app.route('/')
# def index():
#     return render_template('index.html', title='Home', players=players)

@app.route('/rock/scissors')
def game1():
    return "Player 1 wins by playing rock!"


@app.route('/<player_1_choice>/<player_2_choice>')
def mvp(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = RockPaper(player_1, player_2)
    result = game.check_winner(player_1, player_2)
    if result == "Not a valid choice":
        return "Not a valid choice"
    elif result != None:
        return f"Winner is: {result.name} with {result.choice}"
    else:
        return "It is a Draw"

