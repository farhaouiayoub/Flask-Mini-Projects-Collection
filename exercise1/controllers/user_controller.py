# Contrôleur pour la gestion des utilisateurs
# Ce fichier gère les routes liées aux opérations CRUD pour les utilisateurs

# Blueprint dans Flask est un moyen d'organiser une application en composants réutilisables
# Cela permet de:
# 1. Diviser une grande application en modules plus petits
# 2. Enregistrer des routes avec un préfixe commun
# 3. Définir des templates et des fichiers statiques spécifiques à un module
# 4. Éviter les collisions de noms de routes

# Qu'est-ce que "self" en Python?
# -------------------------------------
# "self" est une convention pour le premier paramètre des méthodes d'instance dans une classe Python.
# Il représente l'instance actuelle de la classe et permet d'accéder à ses attributs et méthodes.
# En Python, "self" doit être explicitement déclaré, contrairement à d'autres langages où il est implicite.
# Exemple:
# class Utilisateur:
#     def __init__(self, nom):
#         self.nom = nom  # "self.nom" fait référence à l'attribut de l'instance
#
#     def saluer(self):
#         return f"Bonjour, je m'appelle {self.nom}"
#
# Note: Dans le code de ce contrôleur, "self" n'apparaît pas directement car nous
# utilisons des fonctions régulières pour les routes Flask et non des méthodes de classe.
# Cependant, "self" est utilisé dans la classe UserModel qui est importée.

from flask import Blueprint, render_template, request, redirect, url_for
from models.user_model import UserModel

# Création d'un blueprint pour les routes utilisateur
user_blueprint = Blueprint('user', __name__)
# Initialisation du modèle utilisateur
user_model = UserModel()

@user_blueprint.route('/')
def index():
    # Récupère tous les utilisateurs depuis le modèle
    users = user_model.get_all_users()
    # Affiche la liste des utilisateurs dans le template index.html
    return render_template('index.html', users=users)

@user_blueprint.route('/add_user', methods=['GET', 'POST'])
def add_user():
    # Traitement du formulaire d'ajout d'utilisateur
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.form['name']
        email = request.form['email']
        # Ajout de l'utilisateur à la base de données
        user_model.add_user(name, email)
        # Redirection vers la page d'accueil après ajout
        return redirect(url_for('user.index'))
    
    # Affichage du formulaire d'ajout d'utilisateur
    return render_template('add_user.html')

@user_blueprint.route('/delete_user/<int:id>')
def delete_user(id):
    # Suppression de l'utilisateur avec l'ID spécifié
    user_model.delete_user(id)
    # Redirection vers la page d'accueil après suppression
    return redirect(url_for('user.index'))
