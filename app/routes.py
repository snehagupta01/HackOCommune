from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user={'username':'sneha'}
    posts=[
        {
            'author':{'username':'sg1'},
            'body':'day1'
        },{
            'author':{'username':'sg2'},
            'body':'day2'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)