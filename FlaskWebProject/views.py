from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
from FlaskWebProject import app
import pyodbc
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient


# Database connection (simple helper)
def get_db_connection():
    conn = pyodbc.connect(app.config["SQL_CONNECTION_STRING"])
    return conn


# Home page → list all articles
@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, author, body, image_url FROM articles"
    )
    articles = [
        {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "body": row[3],
            "image_url": row[4],
        }
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
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            flash(f"Welcome back, {username}!", "success")
            return redirect(url_for("home"))
        flash("Invalid credentials. Please try again.", "danger")

    return render_template("login.html", error=error)


# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))


# View single article
@app.route("/article/<int:article_id>")
def article(article_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, author, body, image_url FROM articles WHERE id=?",
        article_id,
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        article = {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "body": row[3],
            "image_url": row[4],
        }
        return render_template("article.html", article=article)
    return "Article not found", 404


# Create new article
@app.route("/create", methods=["GET", "POST"])
def create_article():
    if "user" not in session:
        flash("You must be logged in to create an article.", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        body = request.form["body"]
        image = request.files.get("image")

        image_url = None
        if image and image.filename != "":
            filename = secure_filename(image.filename)

            # Upload image to Azure Blob
            blob_service = BlobServiceClient.from_connection_string(
                app.config["BLOB_CONNECTION_STRING"]
            )
            container_client = blob_service.get_container_client(
                app.config["BLOB_CONTAINER"]
            )
            blob_client = container_client.get_blob_client(filename)
            blob_client.upload_blob(image, overwrite=True)
            image_url = f"{app.config['BLOB_URL']}/{filename}"

        # Save article in DB
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO articles (title, author, body, image_url)
            VALUES (?, ?, ?, ?)
            """,
            (title, author, body, image_url),
        )
        conn.commit()
        conn.close()

        flash("Article created successfully!", "success")
        return redirect(url_for("home"))

    return render_template("create.html")
