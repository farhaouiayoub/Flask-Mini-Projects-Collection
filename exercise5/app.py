from flask import Flask
from models.database import db
from controllers.book_controller import book_blueprint
from models.book_model import Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Register blueprints
app.register_blueprint(book_blueprint)

# Create database if it doesn't exist and add sample data
with app.app_context():
    db.create_all()
    
    # Add sample books if the database is empty
    if Book.query.count() == 0:
        sample_books = [
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
            Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960),
            Book(title="1984", author="George Orwell", year=1949),
            Book(title="The Catcher in the Rye", author="J.D. Salinger", year=1951),
            Book(title="Harry Potter and the Philosopher's Stone", author="J.K. Rowling", year=1997)
        ]
        
        db.session.add_all(sample_books)
        db.session.commit()
        print("Sample books added to database!")

if __name__ == '__main__':
    app.run(debug=True)
