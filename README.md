# Repositorio de Asignacion de Seguridad

Este repositorio contiene ejemplos practicos de aplicaciones web con diferentes niveles de seguridad, disenados para fines educativos dentro de la Asignacion 3.

---

## Estructura del Repositorio

El proyecto se divide en dos secciones principales dentro de la carpeta seguridad/:

### 1. [App Insegura (Vulnerable)](./seguridad/insecure-app/README.md)
Una aplicacion Flask basica que demuestra vulnerabilidades criticas como:
- Inyeccion SQL: Manipulacion de consultas SQL a traves del formulario de login.
- Manejo inseguro de datos: Falta de saneamiento de entradas.
- Configuracion de base de datos: Uso de credenciales por defecto.

### 2. App Segura
Una version mejorada de la aplicacion que implementa mejores practicas de seguridad:
- Consultas Parametrizadas: Prevencion de Inyeccion SQL.
- Hashing de contrasenas: Uso de bcrypt para almacenar contrasenas de forma segura.
- Saneamiento de entradas: Limpieza de datos recibidos del usuario.

---

## Requisitos previos

Para poder ejecutar cualquiera de las aplicaciones, asegurate de tener instalado:
- Docker Desktop
- Docker Compose

---

## Como empezar

Para correr cualquiera de las aplicaciones, navega al directorio correspondiente y usa docker-compose:

cd seguridad/insecure-app
docker-compose up --build

Una vez levantada, la aplicacion estara disponible en http://localhost:5000.

---

## Pruebas y Experimentos

Este repositorio esta disenado para que experimentes con herramientas de seguridad. Puedes probar ataques de SQL Injection en la insecure-app y ver como fallan en la secure-app.

Consulte el [README de la app insegura](./seguridad/insecure-app/README.md) para mas detalles sobre como realizar pruebas de inyeccion.

---

### Autor
Proyecto desarrollado para la asignacion de seguridad informatica.
