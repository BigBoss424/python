from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Aaron'}
    posts = [
        {
            'author':{'username':'Aaron'},
            'body': 'Beautiful day in South El Monte!'
        },
        {
            'author':{'username':'Erin'},
            'body': 'I like Star Wars!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

