from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import User
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!')
            return redirect(url_for('auth.register'))
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please login.')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['username'] = username
            return redirect(url_for('auth.index'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@auth_blueprint.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))
