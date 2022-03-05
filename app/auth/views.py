from flask import render_template
from . import auth
from flask import render_template,redirect,url_for
from ..models import User
from .forms import RegistrationForm
from .. import db
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user
from ..models import User
from .forms import LoginForm,RegistrationForm
@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)