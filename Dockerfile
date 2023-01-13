# pull official base image
FROM python:3.8-slim

# set work directory
RUN mkdir /app
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# copy the application code
COPY . /app
