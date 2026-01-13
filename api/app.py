from flask import Flask, request, escape
import hashlib
import subprocess

app = Flask(__name__)

ADMIN_PASSWORD_HASH = hashlib.sha256("123456".encode()).hexdigest()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "admin" and hash_password(password) == ADMIN_PASSWORD_HASH:
        return "Logged in"
    return "Invalid credentials"

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    result = subprocess.check_output(["ping", "-c", "1", host])
    return result

@app.route("/hello")
def hello():
    name = escape(request.args.get("name", "user"))
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.run(debug=False)
