from flask import Blueprint, jsonify, request
from models.book_model import Book
from models.database import db

book_blueprint = Blueprint('book', __name__)

@book_blueprint.route('/')
def home():
    return jsonify({
        'name': 'Book API',
        'description': 'A RESTful API for managing books',
        'endpoints': {
            'GET /books': 'Get all books',
            'GET /books/<id>': 'Get a specific book by ID',
            'POST /books': 'Add a new book',
            'DELETE /books/<id>': 'Delete a book by ID'
        }
    })

@book_blueprint.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@book_blueprint.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

@book_blueprint.route('/books', methods=['POST'])
def add_book():
    data = request.json
    
    new_book = Book(
        title=data['title'],
        author=data['author'],
        year=data['year']
    )
    
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify(new_book.to_dict()), 201

@book_blueprint.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    
    return jsonify({'message': f'Book with id {id} deleted successfully'}), 200
