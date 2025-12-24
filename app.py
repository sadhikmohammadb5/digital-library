from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "cs50-library-secret"


# ---------- DATABASE ----------
def get_db():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------- HOME + SEARCH ----------
@app.route("/")
def index():
    db = get_db()
    query = request.args.get("q")

    if query and query.strip():
        books = db.execute(
            """
            SELECT id, title, author, category, cover_url
            FROM books
            WHERE title LIKE ? OR author LIKE ?
            """,
            (f"%{query}%", f"%{query}%")
        ).fetchall()
    else:
        books = db.execute(
            "SELECT id, title, author, category, cover_url FROM books LIMIT 6"
        ).fetchall()

    return render_template("index.html", books=books, query=query)


# ---------- REGISTER ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmation = request.form["confirmation"]

        if password != confirmation:
            return "Passwords do not match"

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                (username, generate_password_hash(password))
            )
            db.commit()
        except:
            return "Username already exists"

        return redirect("/login")

    return render_template("register.html")


# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        if user and check_password_hash(user["hash"], password):
            session["user_id"] = user["id"]
            return redirect("/books")

        return "Invalid username or password"

    return render_template("login.html")


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------- ALL BOOKS ----------
@app.route("/books")
def books():
    db = get_db()
    books = db.execute("SELECT * FROM books").fetchall()
    return render_template("books.html", books=books)


# ---------- READ BOOK ----------
@app.route("/read/<int:book_id>")
def read(book_id):
    db = get_db()
    book = db.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    if not book:
        return "Book not found"

    return render_template("read.html", book=book)


# ---------- BORROW ----------
@app.route("/borrow/<int:book_id>")
def borrow(book_id):
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    db.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
    db.execute(
        "INSERT INTO borrows (user_id, book_id, date) VALUES (?, ?, ?)",
        (session["user_id"], book_id, datetime.now().strftime("%Y-%m-%d"))
    )
    db.commit()

    return redirect("/history")

#---------unborrow ----------
@app.route("/unborrow/<int:book_id>")
def unborrow(book_id):
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    db.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
    db.execute(
        "DELETE FROM borrows WHERE user_id = ? AND book_id = ?",
        (session["user_id"], book_id)
    )
    db.commit()

    return redirect("/history")



# ---------- HISTORY ----------
@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    history = db.execute(
        """
        SELECT books.id, books.title, books.author, borrows.date, books.cover_url, books.category
        FROM borrows
        JOIN books ON borrows.book_id = books.id
        WHERE borrows.user_id = ?
        """,
        (session["user_id"],)
    ).fetchall()

    return render_template("history.html", history=history)


if __name__ == "__main__":
    app.run(debug=True)