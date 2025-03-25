from flask import Blueprint, render_template, request, redirect, url_for
from models.user_model import UserModel

user_blueprint = Blueprint('user', __name__)
user_model = UserModel()

@user_blueprint.route('/')
def index():
    users = user_model.get_all_users()
    return render_template('index.html', users=users)

@user_blueprint.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user_model.add_user(name, email)
        return redirect(url_for('user.index'))
    
    return render_template('add_user.html')

@user_blueprint.route('/delete_user/<int:id>')
def delete_user(id):
    user_model.delete_user(id)
    return redirect(url_for('user.index'))
