from flask import render_template,request,redirect,url_for,abort
from ..models import Reviews, User
# from app import auth
from . import main
from flask_login import login_required
from flask_login import login_user,logout_user,login_required
#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))