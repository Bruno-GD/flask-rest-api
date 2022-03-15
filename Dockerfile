FROM python:3.9-alpine
MAINTAINER Bruno Golomb "bgolombduran@cifpfbmoll.eu"

# Expose port 5000 for Flask server
EXPOSE 5000/udp
EXPOSE 5000/tcp
# Install mariadb-connectors
RUN apk add mariadb-connector-c mariadb-connector-c-dev build-base
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
# Set working directory at /app
WORKDIR /app
# Install Python dependencies for this
RUN pip install -r requirements.txt
# Copy all files to /app (working directory)
COPY . /app