from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def hello_world():
    context = {
        'title': 'Fav Five',
        'warriors' : "Josh's Faves",
        'items': {
            1. "sniper",
            2. "sword",
            3. "strategist",
            4. "Leadership",
        }
    }
    return render_template('index.html', title=title)


@app.route('/fav-5')
def fav_5():
    context = {
        'title': "Fav 5 warriors",
        'Pre-eminent warriors': {
            1. 'Simo Häyhä the White Death'
            2. 'Miyamoto Musashi'
            3. 'Alexander the Great'
            4. "Leonithas Dual-King of Sparta"
            5. 'William the Lionheart battle of Acre'
        }


    }
    
    return render_template('fav-5.html', **context)