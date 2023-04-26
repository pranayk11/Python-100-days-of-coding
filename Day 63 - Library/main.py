import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

'''############################ USING SQLITE3 ######################################'''

# db = sqlite3.connect("books-collection.db")  # Creates a new database
# cursor = db.cursor()  # Creates cursor which controls our database
#
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
#                "title varchar(250) NOT NULL UNIQUE,"
#                "author varchar(250) NOT NULL,"
#                "rating FLOAT NOT NULL)")

'''######################### USING SQLALCHEMY ###############################'''
app = Flask(__name__)

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///books-collection.db'
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create Table

with app.app_context():
    class Books(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), unique=True, nullable=False)
        author = db.Column(db.String(100), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        # Optional: this will allow each book object to be identified by its title when printed.
        def __repr__(self):
            return f'<Book {self.title}>'

    db.create_all()

    # # Create RECORD
    # new_book = Books(id=1, title="Harry Potter", author="J.K Rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()

    # READ ALL RECORDS
    all_books = db.session.query(Books).all()
    # print(all_books)

    # READ PARTICULAR RECORD BY QUERY
    book = Books.query.filter_by(title="Harry Potter").first()
    # print(book)

    # UPDATE PARTICULAR RECORD BY QUERY
    book_to_update = Books.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

    # UPDATE RECORD BY PRIMARY KEY
    book_id = 1
    book_to_update = Books.query.get(book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire."
    db.session.commit()

    # DELETE PARTICULAR RECORD BY PRIMARY KEY
    book_id = 1
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()






