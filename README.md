Next env variables are required to start docker compose  
1. `DEBUG` # 1 or 0
2. `SECRET_KEY`  # some complex string
3. `DJANGO_ALLOWED_HOSTS` # localhost,0.0.0.0,127.0.0.1
4. `DB_ENGINE` # django.db.backends.postgresql or any other
5. `DB_DATABASE` # your db name
6. `DB_USER` # your user name
7. `DB_PASSWORD` # your complex password name
8. `DB_HOST` # `db` if running in docker or `localhost` if running locally 
9. `DB_PORT`  # 5432 or whatever

add this information to `.env` file in the root of project and then run
`docker-compose up`