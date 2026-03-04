
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Login Vulnerable</h2>
        <form action="/login">
            Usuario: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="vulnerabledb"
    )

    cursor = conn.cursor()

    # ❌ VULNERABLE A SQL INJECTION
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Consulta ejecutada:", query)

    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        return "Login exitoso"
    else:
        return "Login fallido"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)