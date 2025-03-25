# Flask Projects Collection - MVC Architecture

Bienvenue dans ma collection de projets Flask utilisant l'architecture **MVC** ! 🎉

Cette collection contient plusieurs exercices conçus pour pratiquer le développement web avec **Flask**, **SQLAlchemy** et **SQLite**, tout en suivant l'architecture **Modèle-Vue-Contrôleur (MVC)** pour une meilleure organisation du code.

---

## 📋 Table des matières

1. [Exercice 1 : Gestion des utilisateurs avec Flask (MVC)](#exercice-1-gestion-des-utilisateurs-avec-flask-mvc)
2. [Exercice 2 : Application de liste de tâches (To-Do List) avec Flask (MVC)](#exercice-2-application-de-liste-de-tâches-to-do-list-avec-flask-mvc)
3. [Exercice 3 : Système d'authentification avec Flask (MVC)](#exercice-3-système-dauthentification-avec-flask-mvc)
4. [Exercice 4 : Blog avec Flask (MVC)](#exercice-4-blog-avec-flask-mvc)
5. [Exercice 5 : API RESTful pour la gestion des livres avec Flask (MVC)](#exercice-5-api-restful-pour-la-gestion-des-livres-avec-flask-mvc)
6. [Exercice 6 : Générateur de citations en arabe avec Flask (MVC)](#exercice-6-générateur-de-citations-en-arabe-avec-flask-mvc)

---

## 🚀 Exercice 1 : Gestion des utilisateurs avec Flask (MVC)

**Objectif** : Gérer les utilisateurs avec Flask en suivant l'architecture **MVC**. Utilisation de modèles HTML pour afficher les informations des utilisateurs et une base de données SQLite pour les stocker.

- 📂 **Modèle** : `user_model.py`  
- 📂 **Vue** : `index.html`, `add_user.html`  
- 📂 **Contrôleur** : `user_controller.py`  
- 🛠️ **Technologies utilisées** : Flask, SQLite, MVC

---

## ✅ Exercice 2 : Application de liste de tâches (To-Do List) avec Flask (MVC)

**Objectif** : Créer une application de gestion de tâches en utilisant **SQLAlchemy** avec l'architecture **MVC**. Les utilisateurs peuvent ajouter et supprimer des tâches.

- 📂 **Modèle** : `task_model.py`  
- 📂 **Vue** : `index.html`, `add_task.html`  
- 📂 **Contrôleur** : `task_controller.py`  
- 🛠️ **Technologies utilisées** : Flask, SQLAlchemy, SQLite, MVC

---

## 🔒 Exercice 3 : Système d'authentification avec Flask (MVC)

**Objectif** : Implémenter un système d'authentification complet (enregistrement, connexion et déconnexion des utilisateurs) avec **Flask**, **SQLAlchemy** et **MVC** pour une meilleure organisation du code.

- 📂 **Modèle** : `user_model.py`  
- 📂 **Vue** : `login.html`, `register.html`, `dashboard.html`  
- 📂 **Contrôleur** : `auth_controller.py`  
- 🛠️ **Technologies utilisées** : Flask, SQLAlchemy, HTML, MVC

---

## 📝 Exercice 4 : Blog avec Flask (MVC)

**Objectif** : Créer un blog où les utilisateurs peuvent créer, afficher et lire des articles. Ce projet utilise **SQLAlchemy** et **Flask**, avec l'architecture **MVC** pour séparer les modèles, vues et contrôleurs.

- 📂 **Modèle** : `post_model.py`  
- 📂 **Vue** : `index.html`, `add_post.html`, `view_post.html`  
- 📂 **Contrôleur** : `blog_controller.py`  
- 🛠️ **Technologies utilisées** : Flask, SQLAlchemy, HTML, MVC

---

## 🌍 Exercice 5 : API RESTful pour la gestion des livres avec Flask (MVC)

**Objectif** : Construire une API RESTful pour gérer les livres en suivant l'architecture **MVC**. Les utilisateurs peuvent effectuer des opérations CRUD (Créer, Lire, Supprimer) sur les livres.

- 📂 **Modèle** : `book_model.py`  
- 📂 **Vue** : API RESTful (JSON)  
- 📂 **Contrôleur** : `book_controller.py`  
- 🛠️ **Technologies utilisées** : Flask, SQLAlchemy, API REST, MVC

---

## 💬 Exercice 6 : Générateur de citations en arabe avec Flask (MVC)

**Objectif** : Créer un générateur de citations en arabe qui affiche des citations aléatoires extraites d'une base de données SQLite, avec l'architecture **MVC** pour structurer le projet.

- 📂 **Modèle** : `quote_model.py`  
- 📂 **Vue** : `index.html`  
- 📂 **Contrôleur** : `quote_controller.py`  
- 🛠️ **Technologies utilisées** : Flask, SQLite, MVC

---

## ⚙️ Prérequis

Avant de commencer, assurez-vous d'avoir installé les dépendances suivantes :

- **Python 3.x** ou supérieur
- **Flask**
- **SQLAlchemy**
- **SQLite** (généralement inclus dans Python)

Installez les dépendances en utilisant `pip` :

```bash
pip install flask flask-sqlalchemy
