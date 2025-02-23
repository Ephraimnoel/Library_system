from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style='text-align: center;'>Welcome to LibraryPro</h1>
    <div style='text-align: center;'>
        <h2>Library Management System</h2>
        <p>Created by:</p>
        <ul style='list-style: none;'>
            <li>EPHRAIM NOEL (CIT/00156/022)</li>
            <li>MALIT SOLOMON (CIT/00155/022)</li>
        </ul>
        <p><a href='/about'>About Us</a></p>
    </div>
    """

@app.route('/about')
def about():
    return """
    <div style='text-align: center;'>
        <h1>About LibraryPro</h1>
        <h2>Project Team:</h2>
        <ul style='list-style: none;'>
            <li>EPHRAIM NOEL (CIT/00156/022) - Lead Developer</li>
            <li>MALIT SOLOMON (CIT/00155/022) - Backend Developer</li>
        </ul>
        <p>A Library Management System for Kabarak University</p>
        <p><a href='/'>Back to Home</a></p>
    </div>
    """

if __name__ == '__main__':
    app.run()
