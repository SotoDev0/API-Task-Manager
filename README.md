# API Task Manager

API REST para gestion de tareas con autenticación JWT, construida con FastAPI y SQLite.

## Tecnologías

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)

## Instalación 

1. Clona el repositorio
2. Crea un entorno virtual e instala las dependencias:

```bash
py -3.12 -m virtualenv entorno
entorno\Scripts\activate
pip install -r requirements.txt
```

3. Crea un archivo `.env` en la raíz:

4. Levanta el servidor:
```bash
python -m uvicorn app.main:app --reload
```

## Estado

Proyecto de aprendizaje para practicar FastAPI, autenticación JWT y operaciones CRUD con SQLAlchemy.
