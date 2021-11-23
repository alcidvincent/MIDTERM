from flask import Flask, request, render_template
import sqlite3
import hashlib
app = Flask(__name__)
db_name = 'accounts.db'

@app.route("/")
@app.route("/login")
def main():
    return render_template("login.html")

@app.route("/login2", methods=['POST'])
def login2():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)