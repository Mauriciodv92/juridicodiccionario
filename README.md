
# Diccionario Jurídico 🏛️

Este es un proyecto web desarrollado con **Flask** y **MongoDB**, diseñado para consultar, administrar y gestionar términos jurídicos. La aplicación incluye una interfaz pública y un panel de administración seguro, con soporte para despliegue en Docker.

---

## 📚 Funcionalidades

### 🔍 Interfaz pública:
- Listado de términos jurídicos.
- Buscador interactivo.
- Visualización de imágenes y videos.
- Compatible con tema claro/oscuro.
- Acceso al Manual de Usuario.

### 🔐 Panel de administración:
- Autenticación de usuario administrador.
- CRUD completo de términos (crear, editar, eliminar).
- Carga de imágenes y videos asociados.
- Interfaz adaptada con diseño moderno (Material Design).

---

## 🚀 Tecnologías usadas

- Python 3.11
- Flask
- Flask-PyMongo
- MongoDB
- HTML5 + CSS3 (Material Design inspirado)
- Docker & Docker Compose

---

## 🐳 Despliegue con Docker

### Paso 1: Clona el repositorio
```bash
git clone https://github.com/tu-usuario/diccionario-juridico.git
cd diccionario-juridico
```

### Paso 2: Construye y levanta los contenedores
```bash
docker-compose build
docker-compose up
```

### Acceso en navegador
```
http://localhost:5000
```

---

## ⚙️ Variables de entorno

Asegúrate de que tu archivo `config.py` esté preparado para leer la URI desde una variable:

```python
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/diccionariojuridico")
```

Esta URI es pasada automáticamente desde `docker-compose.yml`.

---

## 👤 Credenciales de acceso

Por defecto, deberás definir tus propias credenciales en el validador de autenticación del panel de administrador (`utils/auth.py`).

---

## 📂 Estructura recomendada

```
juridicodiccionario/
├── app.py
├── config.py
├── controllers/
│   ├── admin_controller.py
│   └── client_controller.py
├── models/
│   └── termino.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   └── manual_usuario.html
├── static/
│   ├── style.css
│   └── uploads/
```

---

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT.

---

## ✨ Contribuciones

Si deseas contribuir, ¡haz un fork y crea tu pull request!

---
