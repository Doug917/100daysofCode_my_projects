'''

This project consists of updating and rendering
a simple website with Flask and SQLite3 that shows
a list of books that the user can add to.
Most of this code I copied from Angela from Day 63 of
100 days of code.

The difference is that I use SQLite exclusively with JSON
instead of SQalchemy.


'''


from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import json

all_books = []

db = sqlite3.connect("books_database.db")
curr = db.cursor()


curr.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

#Populate all_books dictionary with data from database.
for row in curr.execute("SELECT * FROM books"):
    all_books.append({"title": row[0], "author": row[1], "rating": row[3]})


curr.close()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        
        all_books.append(new_book)
        new_book_j = json.dumps(new_book, indent=4)

        #Add new book info to database.
        with sqlite3.connect("books_database.db") as db:
            curr = db.cursor()
            curr.execute("Insert into books (title, author, rating) values (:title, :author, :rating)", json.loads(new_book_j))
            db.commit()
        
        #NOTE: You can use the redirect method from flask to redirect to another route 
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
      
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

