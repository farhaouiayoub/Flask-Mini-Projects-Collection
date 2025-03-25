from flask import Flask
from models.database import db
from controllers.auth_controller import auth_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

# Initialize the database with the app
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_blueprint)

# Create database if it doesn't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
