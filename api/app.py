from flask import Flask, request
import hashlib
import subprocess

app = Flask(__name__)

ADMIN_PASSWORD = "123456"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "admin" and hash_password(password) == hash_password(ADMIN_PASSWORD):
        return "Logged in"
    return "Invalid credentials"

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result

@app.route("/hello")
def hello():
    name = request.args.get("name", "user")
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
