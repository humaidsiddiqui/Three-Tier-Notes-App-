from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-note', methods=['POST'])
def submit_note():
    try:
        data = request.get_json()  # Get JSON data from the request
        if not data or 'title' not in data or 'content' not in data:
            return jsonify({'error': 'Title and content are required!'}), 400

        title = data['title']
        content = data['content']

        print(f"Received data: title={title}, content={content}")  # Debugging

        note = Note(title=title, content=content)
        db.session.add(note)
        db.session.commit()

        return jsonify({'message': 'Note added successfully!', 'title': title, 'content': content}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Database error: {e}")
        return jsonify({'error': str(e)}), 500
   
@app.route("/delete-note", methods=['POST'])
def delete_record():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    note = Note.query.filter_by(title=title, content=content).first()
    if note:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"success": True}), 200
    return jsonify({"error": "Note not found"}), 404
def delete():
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000) 