import os
import json
from flask import Flask, request, render_template, url_for

# from dotenv import load_dotenv

from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
    user=os.getenv("POSTGRES_USER"),
    passwd=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=5432,
    table=os.getenv("POSTGRES_DB"),
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserModel(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


# load_dotenv()

f = open("./lavina.json")
data = json.load(f)
f.close()


@app.route("/")
def index():
    return render_template("index.html", title="MLH Fellow", url=os.getenv("URL"))


@app.route("/health")
def health():
    return render_template(
        "data.html",
        data=data,
        main="Accomplishments",
        side1="Experience",
        side2="Projects",
        url=os.getenv("URL"),
    )


# @app.route("/")
@app.route("/Experience/")
def experience():
    return render_template(
        "data.html",
        data=data,
        main="Experience",
        side1="Projects",
        side2="Accomplishments",
        url=os.getenv("URL"),
    )


@app.route("/Projects/")
def projects():
    return render_template(
        "data.html",
        data=data,
        main="Projects",
        side1="Experience",
        side2="Accomplishments",
        url=os.getenv("URL"),
    )


@app.route("/Accomplishments/")
def accomplishments():
    return render_template(
        "data.html",
        data=data,
        main="Accomplishments",
        side1="Experience",
        side2="Projects",
        url=os.getenv("URL"),
    )


# for database
@app.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif UserModel.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."

        if error is None:
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"

        else:
            return error, 418

    ## TODO: Return a restister page
    return render_template("register.html", title="register")


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        error = None

        if user is None:
            error = "Incorrect username."

        elif not check_password_hash(user.password, password):
            error = "Incorrect password."
        if error is None:
            return "Login Successful", 200
        else:
            return error, 418

    ## TODO: Return a login page
    return render_template("login.html", data=data, mode="login")
