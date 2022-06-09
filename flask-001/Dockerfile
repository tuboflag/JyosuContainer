FROM python:3.9.7-slim-buster

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY app/requirements.txt ./
RUN apt-get update
RUN apt-get install -y python3-pip
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
