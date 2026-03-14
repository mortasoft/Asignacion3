# 🛡️ Secure Lab | Universidad Cenfotec

Este es el entorno **mitigado** del laboratorio de seguridad. A diferencia de la versión vulnerable, este portal implementa medidas defensivas estándar de la industria para prevenir ataques de **Inyección SQL** y proteger la integridad de las credenciales de los usuarios.

---

## 🔒 Mecanismos de Defensa Implementados

### 1. Consultas Parametrizadas (Prepared Statements)
Se utiliza el conector de MySQL con placeholders (`%s`) para separar la lógica de la consulta SQL de los datos proporcionados por el usuario.
```python
# ✅ Código Seguro
query = "SELECT password FROM users WHERE username = %s"
cursor.execute(query, (username,))
```
Esto garantiza que cualquier carácter especial (como `' OR '1'='1`) sea tratado como texto plano y no como código ejecutable.

### 2. Criptografía con BCrypt
Las contraseñas no se almacenan en texto plano. Se procesan usando `bcrypt`, un algoritmo de hashing diseñado para ser resistente a ataques de fuerza bruta y tablas de arcoiris (Rainbow Tables).
- **Salteo (Salting):** Cada hash incluye un salt único generado aleatoriamente.
- **Factor de Trabajo:** Configurado para balancear seguridad y rendimiento.

### 3. Manejo de Errores Genéricos
El sistema no revela detalles sobre si el usuario existe o no en caso de fallo, ni muestra logs de errores de la base de datos al usuario final, evitando la **enumeración de usuarios**.

---

## 🚀 Despliegue del Entorno Seguro

Para levantar este entorno de forma independiente:

```powershell
cd seguridad/secure-app
docker-compose up -d --build
```

**URL de acceso:** [http://localhost:5001](http://localhost:5001)

---

## 🧪 Pruebas Sugeridas

1.  **Validación de Bypass:** Intente ingresar con `' OR '1'='1` en el campo de usuario. El sistema rechazará la entrada ya que busca literalmente un usuario llamado `' OR '1'='1`.
2.  **Registro y Hash:** Regístrese con un nuevo usuario y observe la base de datos. Verá que la columna `password` contiene un hash irreconocible (ej. `$2b$12$...`).
3.  **Seguridad de Capa:** Observe que el formulario utiliza el método `POST` para evitar que las credenciales queden expuestas en los logs del servidor web o en el historial del navegador.

---

## 📁 Estructura del Módulo

- `app.py`: Servidor Flask endurecido.
- `templates/`: UI con temática Emerald (Seguro).
- `init.sql`: Esquema de base de datos con restricciones de unicidad.
- `requirements.txt`: Incluye `bcrypt` y `mysql-connector-python`.

---
*Módulo de Mitigación - Universidad Cenfotec 2026.*
