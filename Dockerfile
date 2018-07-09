# this is an official Python runtime, used as the parent image
FROM python:3.7.0-alpine3.7

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# the following adds the pg_config executable
RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "app.py"]

# docker build -t cjoakim/webapp-docker-python . 
# docker run -d -e PORT=8080 -p 8080:8080 cjoakim/webapp-docker-python:latest
