from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # En un entorno real usaríamos POST, pero para fines educativos de seguridad 
    # se mantiene GET para observar los parámetros en la URL o se acepta ambos.
    username = request.args.get('username') or request.form.get('username')
    password = request.args.get('password') or request.form.get('password')

    if not username or not password:
        return redirect(url_for('home'))

    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="vulnerabledb"
        )
        cursor = conn.cursor()

        # ❌ VULNERABLE A SQL INJECTION - PARA PROPÓSITOS EDUCATIVOS
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Ejecutando consulta:", query)

        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if result:
            return render_template('login.html', success=True, user=username)
        else:
            return render_template('login.html', error="Credenciales inválidas")
            
    except Exception as e:
        return render_template('login.html', error=f"Error de conexión: {str(e)}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)