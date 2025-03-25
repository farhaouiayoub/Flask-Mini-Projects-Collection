from flask import Blueprint, render_template
from models.quote_model import QuoteModel

quote_blueprint = Blueprint('quote', __name__)
quote_model = QuoteModel()

@quote_blueprint.route('/')
def index():
    random_quote = quote_model.get_random_quote()
    return render_template('index.html', quote=random_quote)
