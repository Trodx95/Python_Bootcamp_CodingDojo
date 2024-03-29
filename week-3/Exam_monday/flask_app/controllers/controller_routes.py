from flask_app import app 
from flask import render_template, redirect,session,request

from flask_app.models import model_show , model_user

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    context = {
        'all_shows': model_show.Show.get_all(),
        'user': model_user.User.get_one({'id' : session ['uuid']})
    }
    return render_template('dashboard.html' , **context)