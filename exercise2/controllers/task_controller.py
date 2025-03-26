from flask import Blueprint, render_template, request, redirect, url_for
from models.task_model import Task
from models.database import db

task_blueprint = Blueprint('task', __name__) 

@task_blueprint.route('/')
def index():
    tasks = Task.query.all() # Récupère toutes les tâches depuis la base de données
    return render_template('index.html', tasks=tasks)

@task_blueprint.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        new_task = Task(title=title)
        db.session.add(new_task) # Ajoute la nouvelle tâche à la session
        db.session.commit() # Valide les changements dans la base de données
        return redirect(url_for('task.index'))
    return render_template('add_task.html')

@task_blueprint.route('/delete_task/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task.index'))


@task_blueprint.route('/toggle_done/<int:id>', methods=['POST'])
def toggle_done(id):
    task = Task.query.get_or_404(id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('task.index'))




# Dans Flask (un framework Python), un Blueprint est un moyen d'organiser une application en plusieurs modules.

# Il permet de structurer une grande application en plusieurs parties réutilisables.

# Exemple : un Blueprint pour gérer l'authentification, un autre pour le tableau de bord, etc.
