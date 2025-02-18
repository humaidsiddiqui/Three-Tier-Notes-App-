from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#postgresl database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#database model for notes
class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    def __init__(self, title, content):
        self.title = title
        self.content = content
@app.route('/')
def index():
    # notes = Note.query.all()
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            note = Note(title, content)
            db.session.add(note)
            db.session.commit()
        return redirect(url_for('index'))
 
if __name__ == '__main__':
    app.run(debug=True)
