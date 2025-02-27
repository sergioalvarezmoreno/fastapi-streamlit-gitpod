# Aplicación de Gestión de Usuarios con FastAPI y Streamlit

Esta es una aplicación sencilla para gestionar usuarios, desarrollada con FastAPI para el backend y Streamlit para el frontend. La aplicación permite registrar usuarios con DNI y nombre, así como consultar la información de los usuarios registrados.

## Características

- API RESTful con FastAPI
- Base de datos SQLite para almacenamiento persistente
- Frontend interactivo con Streamlit
- Despliegue automatizado en Gitpod

## Estructura del Proyecto

- `app.py`: API FastAPI con endpoints para gestionar usuarios
- `frontend.py`: Interfaz de usuario con Streamlit
- `requirements.txt`: Dependencias del proyecto
- `start.sh`: Script para iniciar tanto la API como el frontend
- `.gitpod.yml`: Configuración para despliegue en Gitpod

## Endpoints de la API

- `POST /usuarios/`: Registra un nuevo usuario
- `GET /usuarios/`: Obtiene la lista de todos los usuarios
- `GET /usuarios/{dni}`: Obtiene la información de un usuario específico por su DNI

## Cómo ejecutar la aplicación en Gitpod

1. Haz clic en el botón "Open in Gitpod" a continuación para abrir el proyecto en Gitpod:

   [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/sergioalvarezmoreno/fastapi-streamlit-gitpod)

2. Gitpod configurará automáticamente el entorno y ejecutará la aplicación.
3. Se abrirán automáticamente dos pestañas en el navegador:
   - La API FastAPI en el puerto 8000
   - El frontend de Streamlit en el puerto 8501

## Ejecución Local

Si prefieres ejecutar la aplicación localmente:

1. Clona este repositorio
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el script de inicio: `bash start.sh`

## Tecnologías Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Framework moderno y rápido para construir APIs con Python
- [Streamlit](https://streamlit.io/): Framework para crear aplicaciones web interactivas con Python
- [SQLAlchemy](https://www.sqlalchemy.org/): ORM SQL para Python
- [Gitpod](https://www.gitpod.io/): Entorno de desarrollo en la nube
