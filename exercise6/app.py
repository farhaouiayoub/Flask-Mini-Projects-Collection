from flask import Flask
from controllers.quote_controller import quote_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(quote_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
