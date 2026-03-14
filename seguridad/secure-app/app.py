from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
import bcrypt
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="securedb"
    )

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return render_template("login.html", error="Cualquier campo es requerido.")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # ✅ CONSULTA PARAMETRIZADA - PREVIENE SQL INJECTION
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            return render_template("login.html", success=True, user=username)
        else:
            return render_template("login.html", error="Credenciales incorrectas o usuario no encontrado.")
            
    except Exception as e:
        return render_template("login.html", error=f"Error de sistema: {str(e)}")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            return render_template("register.html", error="Todos los campos son obligatorios.")

        # Hashing de la contraseña
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, hashed))
            conn.commit()
            conn.close()
            return render_template("login.html", success_msg="Registro exitoso. Ahora puedes iniciar sesión.")
        except mysql.connector.Error as err:
            return render_template("register.html", error=f"Error: El usuario ya existe o hubo un fallo en BD.")
    
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)