from flask import render_template, request, redirect, url_for, session
from FlaskWebProject import app, logger
import pyodbc

# Database connection (simple helper)
def get_db_connection():
    conn = pyodbc.connect(app.config['SQL_CONNECTION_STRING'])
    return conn

# Home page → list all articles
@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, body FROM articles")
    articles = [
        {"id": row[0], "title": row[1], "author": row[2], "body": row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return render_template("home.html", articles=articles)

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            logger.info(f"✅ User {username} logged in successfully")
            return redirect(url_for("home"))
        else:
            logger.warning("❌ Invalid login attempt")
            error = "Invalid credentials. Please try again."

    return render_template("login.html", error=error)

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

# View single article
@app.route("/article/<int:article_id>")
def article(article_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, body FROM articles WHERE id=?", article_id)
    row = cursor.fetchone()
    conn.close()
    if row:
        article = {"id": row[0], "title": row[1], "author": row[2], "body": row[3]}
        return render_template("article.html", article=article)
    else:
        return "Article not found", 404
