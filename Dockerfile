FROM python:3.8.2-alpine3.11

COPY ./app/ /app

COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD gunicorn main:api -c gunicorn_settings.py
