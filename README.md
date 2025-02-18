# Notes App - Flask & PostgreSQL

A simple **Notes App** built using **Flask** (Python web framework), **PostgreSQL** (database), and **JavaScript** for dynamic content handling.

## Features
- Add new notes with a title and content.
- Notes are stored in a PostgreSQL database.
- Dynamic note display without page reload using JavaScript Fetch API.

## Tech Stack
- **Backend**: Flask (Python), SQLAlchemy
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Hosting**: Local Development

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- PostgreSQL
- pip (Python package manager)

## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/notes-app.git 
cd notes-
```

##2. Set Up a PostgreSQL Database
Create a PostgreSQL database (e.g., notes):
```bash
Copy
Edit
psql -U postgres
CREATE DATABASE notes;
```

3. Install Dependencies
Install the required Python packages:
```bash
Copy
Edit
pip install -r requirements.txt
```
4. Update Database URI
In app.py, update the SQLALCHEMY_DATABASE_URI to match your PostgreSQL setup:
```bash
python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/notes'
```
5. Create Database Tables
Run the following commands to create the necessary tables:
```bash
Copy
Edit
python
from app import db
db.create_all()
```
6. Start the Flask App
Run the Flask application:

```bash
Copy
Edit
python app.py
The app will be running at http://127.0.0.1:5000/.
