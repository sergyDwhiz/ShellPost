from flask import Flask
from routes.email_routes import email_bp
from utils.db import db

# Initialize Flask app and set up SQLAlchemy database connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(email_bp)

db.init.app(app)
app.register_blueprint(email_bp)

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Resource not found'}, 404

@app.errorhandler(500)
def server_error(error):
    return {'error': 'Internal server error'}, 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
