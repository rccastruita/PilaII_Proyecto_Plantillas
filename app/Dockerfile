# Version de python
FROM python:3.9

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# La carpeta en la que se va a trabajar
WORKDIR /usr/src/app

# Dependencias
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pip install pipenv && pipenv install --system

# Copia el proyecto
COPY . .