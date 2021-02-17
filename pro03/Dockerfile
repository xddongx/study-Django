# pull official base image
FROM python:3.8.5-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUMBUFFERED 1

RUN apk update
RUN apk add mysql-dev gcc python3-dev musl-dev jpeg-dev


COPY . /usr/src/app/
# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install django-markdownx
