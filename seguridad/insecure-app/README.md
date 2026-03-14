# AsignacionSeguridad

![banner](./assets/banner.png)

Este es un proyecto educativo disenado para demostrar las diferencias entre una aplicacion vulnerable (insegura) y una segura, enfocandose primordialmente en el ataque de Inyeccion SQL.

---

## Como Correr el App

Para correr esta aplicacion, necesitaras tener Docker y Docker Compose instalados en tu sistema. Segun las reglas de este proyecto, siempre priorizamos el uso de contenedores.

### Pasos para iniciar:

1. Levantar los contenedores:
   Ejecuta el siguiente comando en tu terminal (PowerShell):
   docker-compose up --build

2. Acceder a la aplicacion:
   Una vez que los contenedores esten arriba, abre tu navegador y ve a:
   http://localhost:5000

---

## Como se usa el App

La aplicacion presenta un formulario de login simple. Su proposito es ser vulnerable, por lo que puedes interactuar con ella de las siguientes maneras:

### 1. Login Normal (Legitimo)
Puedes usar las siguientes credenciales predefinidas en el archivo init.sql:
- Usuario: admin / Password: admin123
- Usuario: user1 / Password: password1

### 2. Demostracion de Inyeccion SQL (Ataque)
Para demostrar la vulnerabilidad, intenta ingresar lo siguiente en el campo de Usuario:
admin' --
(Deja el campo de password vacio)

Esto funciona porque la consulta SQL en el backend es vulnerable:
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

Al ingresar admin' --, la consulta se convierte en:
SELECT * FROM users WHERE username = 'admin' --' AND password = ''
El -- comenta el resto de la consulta, permitiendo el ingreso sin contrasena.

---

## Estructura del Proyecto

- app.py: El backend en Flask (Vulnerable).
- Dockerfile: Definicion del contenedor de la aplicacion.
- docker-compose.yml: Orquestacion de la base de datos MySQL y la aplicacion.
- init.sql: Script de inicializacion de la base de datos.
- requirements.txt: Dependencias de Python.

---

## Advertencia de Seguridad
NO UTILICES ESTE CODIGO EN PRODUCCION. El codigo en este directorio esta intencionalmente disenado para ser inseguro para fines educativos.
