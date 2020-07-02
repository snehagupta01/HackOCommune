from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm

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

@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requseted for user={} ,remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In',form=form)