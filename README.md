<<<<<<< HEAD
## What this repo does
This repo is a flask application within docker containers. It uses Nginx to handle client requests and Gunicorn as the WSGI. The server can contain Postgres databases, static files, and media files. Media files can be uploaded by the user in a web browser at http://localhost:1317/upload.

##Build instructions
1. Download all files from repository.\
2. Create the file .env.prod file in the root. It should contain:
```
FLASK_APP=project/__init__.py
FLASK_DEBUG=0
DATABASE_URL=postgresql://hello_flask:hello_flask@db:5432/hello_flask_prod
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
\
3. Create the file .env.prod.db in the root. It should contain:
```
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=hello_flask_prod
```
\
4. Run: 
```
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py create_db

```

<img src='example.gif' width=100%/>
=======
# csci143-final

[![](https://github.com/justinchiao/csci143-final/workflows/web-service/badge.svg)]
>>>>>>> 34cc0396edd239ddca03fea0c309b7849c4c975c
