from flask import Flask, render_template
from models import db, User
from flask_login import LoginManager

app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    return """
    <h1>Welcome to LibraryPro</h1>
    <p>Created by:</p>
    <ul>
        <li>EPHRAIM NOEL (CIT/00156/022)</li>
        <li>MALIT SOLOMON (CIT/00155/022)</li>
    </ul>
    """

@app.route('/about')
def about():
    return """
    <h1>About LibraryPro</h1>
    <h2>Project Team:</h2>
    <ul>
        <li>EPHRAIM NOEL (CIT/00156/022) - Lead Developer</li>
        <li>MALIT SOLOMON (CIT/00155/022) - Backend Developer</li>
    </ul>
    <p>A Library Management System for Kabarak University</p>
    """

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
