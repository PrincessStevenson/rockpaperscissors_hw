from flask import render_template
from app import app
from models.players import *
from models.player_list import *


@app.route('/')
def index():
    return "Shall We Play A Little Game.."

# @app.route('/')
# def index():
#     return render_template('index.html', title='Home', players=players)

@app.route('/rock/scissors')
def game1():
    return "Player 1 wins by playing rock!"