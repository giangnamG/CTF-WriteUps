import sqlite3
from flask import Flask, render_template, Response, request, g, session, redirect
import os
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(120)
FLAG = open("/flag.txt", "r").read()
DATABASE = "data.db"


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_users_table():
    # Create a new SQLite database
    conn = get_db()

    # Create a table in the database
    conn.execute('''CREATE TABLE users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL,
                 description TEXT
                 );''')

    # Insert some sample data into the table
    conn.execute("INSERT INTO users (username, password, description) VALUES (?, ?, ?)",
                 ('admin', get_random_string(30), f"{FLAG}"))
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", ('dog', "bowwow"))
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", ('cat', 'meow'))
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", ('guest', 'guest'))

    # Commit the changes
    conn.commit()


@app.before_first_request
def init_db():
    init_users_table()


@app.route('/')
def index():
    return render_template('welcome.jinja2',
                           title="challenge-name-web-python",
                           description="challenge-name-web-python")


@app.route('/heath')
def heath():
    return "OK"


@app.route('/login', methods=['GET', 'POST'])
def login_sql():
    conn = get_db()
    if request.method == "GET":
        return render_template("login.jinja2")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        query = 'SELECT * FROM users WHERE username=? AND password=?'

        account = conn.execute(query, (username, password)).fetchone()
        if not account:
            return render_template("login.jinja2", popup_message="'Login failed. Please try again.'")

        session["username"] = username
        session["description"] = account["description"]
        return redirect("/account")


@app.route("/account", methods=["GET"])
def account():
    return render_template("account.jinja2")


@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "GET":
        username = request.args.get("username", session.get("username"))
        if not username:
            return redirect("/login")

        conn = get_db()
        user = conn.execute(
            """
                SELECT *
                FROM users
                WHERE username = ?        
            """,
            (username,)
        ).fetchone()
        return render_template("reset_password.jinja2", username=username, password=user["password"])
    if request.method == "POST":
        username = session.get("username")
        if not username:
            return "Not login yet"
        new_password = request.form["new_password"]

        conn = get_db()
        conn.execute(
            """
                UPDATE users
                SET password = ?
                WHERE username = ?
            """,
            (new_password, username)
        )

        return "Update success"


@app.route('/debug')
def debug():
    return Response(open(__file__).read(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=False)