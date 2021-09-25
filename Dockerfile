FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED 1
#Creamos el contenedor que tendrá toda nuestra aplicación
WORKDIR /code
COPY . /code/
#Copiamos nuestros archivos locales a la imagen docker
RUN pip install -r requirements.txt