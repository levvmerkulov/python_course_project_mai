from flask import render_template, flash, redirect, url_for, request
from app import app_name, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime


@app_name.route('/')
@app_name.route('/index')
@login_required
def index():
    posts = [
        'Greenfield software development refers to developing a system \
        for a totally new environment and requires development from a \
        clean slate – no legacy code around. It is an approach used when \
        you’re starting fresh and with no restrictions or dependencies.',

        'A pure Greenfield project is quite rare these days, you frequently \
        end up interacting or updating some amount of existing code or \
        enabling integrations. Some examples of Greenfield software \
        development include: building a website or app from scratch, \
        setting up a new data center, or even implementing a new rules engine.'
    ]
    return render_template('index.html', title = 'Home', posts = posts)

@app_name.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit(): #When click submit
        user = User.query.filter_by(username = form.username.data).first()    
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title = 'Sign In', form = form)

@app_name.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app_name.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit(): #When click submit
        user = User(
            username = form.username.data, 
            email = form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have registered a new account.')
        return redirect(url_for('login'))

    return render_template('register.html', title = 'Sign Up', form = form)

@app_name.route('/user/<username>') # <..> has dynamic content inside
@login_required
def user(username):
    '''profile page'''
    user = User.query.filter_by(username = username).first_or_404()
    return render_template('user.html', user = user)

@app_name.route('/edit_profile', methods = ['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Changes have been saved')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title = 'Edit Profile',
        form = form)