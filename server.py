from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#postgresl database configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#database model for notes  
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Note {self.title}>'
        @app.route('/')
        def index():
            notes = Note.query.all()
            return render_template('index.html', notes=notes)

        @app.route('/add', methods=['POST'])
        def add_note():
            title = request.form['title']
            content = request.form['content']
            new_note = Note(title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('index'))

        @app.route('/update/<int:id>', methods=['GET', 'POST'])
        def update_note(id):
            note = Note.query.get_or_404(id)
            if request.method == 'POST':
                note.title = request.form['title']
                note.content = request.form['content']
                db.session.commit()
                return redirect(url_for('index'))
            return render_template('update.html', note=note)

        @app.route('/delete/<int:id>')
        def delete_note(id):
            note = Note.query.get_or_404(id)
            db.session.delete(note)
            db.session.commit()
            return redirect(url_for('index'))




























