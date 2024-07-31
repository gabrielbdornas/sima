FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY . /app
COPY /etc/secrets/.env /app/.env
RUN pip install -r requirements.txt
RUN python manage.py migrate


ENTRYPOINT [ "gunicorn", "sima.wsgi", "-b", "0.0.0.0:8000"]