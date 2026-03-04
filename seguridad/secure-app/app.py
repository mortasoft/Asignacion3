from flask import Flask, request
import mysql.connector
import bcrypt

app = Flask(__name__)

db = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="securedb"
)

@app.route("/")
def home():
    return '''
        <h2>Login Seguro</h2>
        <form action="/login">
            Usuario: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="login">
        </form>
    '''

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor = db.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, hashed))
    db.commit()

    return "User registered securely"

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    cursor = db.cursor()
    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)