FROM python:3.14


ENV REDIS_URL=redis://redis PYTHONUNBUFFERED=1 BACKEND_PORT=${PORT:-8080}

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt


ENTRYPOINT ["reflex", "run", "--env", "prod", "--backend-only", "--loglevel", "debug" ]
