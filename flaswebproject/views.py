from flask import render_template, request, redirect, url_for, session
from FlaskWebProject import app, logger

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    # TODO: use MSAL for auth
    logger.info("Login attempt")
    return render_template("login.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        body = request.form["body"]
        # TODO: upload image to Azure Blob + insert article in DB
        logger.info(f"Article created: {title} by {author}")
        return redirect(url_for("index"))
    return render_template("create.html")
