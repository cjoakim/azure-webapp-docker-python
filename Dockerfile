FROM python:3

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

RUN python --version
RUN pip --version

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip list

# unblock port 5000 for the Flask app
EXPOSE 5000

# execute the Flask app
CMD ["python", "app.py"]


# docker build -t cjoakim/webapp-docker-python . 
# docker image ls | grep webapp-docker-python
# docker run -d -e PORT=5000 -p 5000:5000 cjoakim/webapp-docker-python:latest
# docker run -d -e PORT=80 -p 80:3000 cjoakim/webapp-docker-python:latest
# docker stop -t 2 008038664a58
# docker exec -it b23d3ce4b830 /bin/bash
#   @b23d3ce4b830:/app# curl -v http://localhost
#   @b23d3ce4b830:/app# curl -v http://localhost/env
#
# docker push cjoakim/webapp-docker-python:latest
#
# docker tag cjoakim/webapp-docker-python:latest cjoakimacr.azurecr.io/webapp-docker-python:latest
# docker push cjoakimacr.azurecr.io/webapp-docker-python:latest
#
# az acr login --name cjoakimacr
# az acr repository list --name cjoakimacr --output table
