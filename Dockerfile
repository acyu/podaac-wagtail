#offical base image
from python:3.8

#set environment variables
#python -B
ENV PYTHONDONTWRITEBYTECODE 1
#python -u
ENV PYTHONUNBUFFERED=1

#create and set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

#install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

