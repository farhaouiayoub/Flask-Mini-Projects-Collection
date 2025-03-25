from flask import Flask
from models.database import db
from controllers.task_controller import task_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Register blueprints
app.register_blueprint(task_blueprint)

# Create database if it doesn't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
