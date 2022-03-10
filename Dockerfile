FROM python:3.9-slim
MAINTAINER Bruno Golomb "bgolombduran@cifpfbmoll.eu"

RUN apt-get update -y && \
    apt-get install -y gcc libmariadb3 libmariadb-dev

EXPOSE 5000/udp
EXPOSE 5000/tcp

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP=flaskr
ENTRYPOINT flask run --host=0.0.0.0 --port=5000