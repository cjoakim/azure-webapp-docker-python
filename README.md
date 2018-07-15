# azure-webapp-docker-python

Azure Web App built with Python and the Flask framework

## What we'll do

1. Configure workstation
1. Develop the app
1. Dockerize the app
1. Deploy as a Docker image to Azure Container Instance
1. Deploy as a Docker image to Azure App Service
1. Deploy as a GitHub repo to a Data Science Virtual Machine (DSVM)
1. Deploy as a Docker image to a Data Science Virtual Machine (DSVM)

---

## 1. Configure workstation

These instructions are for a Linux or macOS workstation.
Alternatively, you could use a remote Linux Data Science Virtual Machine (DSVM).

First, install the Azure CLI (Command Line Interface).
See https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest

Then, execute some CLI commands:
```
$ az

     /\
    /  \    _____   _ _  ___ _
   / /\ \  |_  / | | | \'__/ _\
  / ____ \  / /| |_| | | |  __/
 /_/    \_\/___|\__,_|_|  \___|


Welcome to the cool new Azure CLI!
...

$ az login --help

$ az login
```

Next, download and install Docker Community Edition.
See https://www.docker.com/get-docker

Python 3.x and pip are assumed to be installed.

---

## 2. Develop the app

The application in this repository is a very simple Python3/Flask web application.
It is intended to simply demonstrate deployment to Azure.

---

## 3. Dockerize the app

See the **Dockerfile** which is used to create a **Docker Image** of this app.

Create an **Azure Container Registry** account in Azure Portal, and optionally
a **DockerHub** account at https://hub.docker.com.

See the **Dockerfile** and **build_image.sh**.
Notice how the Dockerfile does a **pip install** into the image.

```
$ docker build -t cjoakim/webapp-docker-python . 

$ docker image ls
```

Test the Docker image locally on your workstation.  The -e parameter is used to
pass environment variables into the executed image.  The -p paramter maps port
5000 in the running image to port 5000 on your workstation.
```
$ docker run -d -e PORT=5000 -p 5000:5000 cjoakim/webapp-docker-python:latest
```

Optionally "ssh" into the running image; first run a ps to get the CONTAINER ID:
```
$ docker ps

$ docker exec -it b23d3ce4b830 /bin/bash
```

Once in the image shell, run these commands, then exit the shell:
```
@b23d3ce4b830:/app# curl -v http://localhost
@b23d3ce4b830:/app# curl -v http://localhost/env
exit
```

Stop the running image:
```
$ docker stop -t 2 b23d3ce4b830
```

Push the image to DockerHub after successfully testing it locally:
```
$ docker push cjoakim/webapp-docker-python:latest
```

Push the image to Azure Container Registry:
```
$ az acr login --name cjoakimacr
$ az acr repository list --name cjoakimacr --output table

$ docker tag cjoakim/webapp-docker-python:latest cjoakimacr.azurecr.io/webapp-docker-python:latest
$ docker push cjoakimacr.azurecr.io/webapp-docker-python:latest

$ az acr repository list --name cjoakimacr --output table
```

---

## 4. Deploy as a Docker image to Azure Container Instance (ACI)

The Azure CLI can be used to do this.

First create an Azure **resource group**:
```
$ az group create --location eastus --name FlaskFun

{
  "id": "/subscriptions/71......4f/resourceGroups/FlaskFun",
  "location": "eastus",
  "managedBy": null,
  "name": "FlaskFun",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null
}
```

Then create the ACI in the new Resource Group:
```
$ az container create --resource-group FlaskFun --name webapp-docker-python --image cjoakimacr.azurecr.io/webapp-docker-python:latest --cpu 1 --memory 1 --registry-username cjoakimacr --registry-password $AZURE_CONTAINER_REGISTRY_USER_PASS --dns-name-label webapp-docker-python --ports 5000 -e 'PORT=5000'

$ az container list
```

Invoke the running ACI with your browser:
- http://webapp-docker-python.eastus.azurecontainer.io:5000/
- http://webapp-docker-python.eastus.azurecontainer.io:5000/env

See content similar to this:
![homepage-img](img/homepage.png "")

---

## 5. Deploy as a Docker image to Azure App Service

In Azure Portal, create a **Web App** of type **Docker** and configure
it to use your image from Azure Container Registry as follows:

![create-img](img/create-webapp-docker-python.png "")

Visit the URL with your browser, for example:
http://webapp-docker-python.eastus.azurecontainer.io:5000/

---

## 6. Deploy as a GitHub repo to a Data Science Virtual Machine

The DSVM contains many common pre-installed Data Science and Developer tools - 
python2, python3, R, git, docker, java, ant, maven, php, ruby, etc.

First, in Azure Portal, provision a **Data Science Virtual Machine for Linux (Ubuntu)**.  Specify your ssh keys.

Then, in the DSVM in Azure Porta, open up port 5000 for Flask via the 
Networking -> Add Inbound Port dialog.

ssh into the VM and execute the following commands:
```
$ git clone git@github.com:cjoakim/azure-webapp-docker-python.git

$ ./venv.sh             <- creates the python virtual environment
$ source bin/activate   <- activate the virtual environment
$ python app.py         <- start the Flask web app
```

Then, visit the URL with your browser:
http://40.76.207.55:5000/

Note: this configuration and deployment process can be automated with **Ansible**.

### conda and Anaconda on the DSVM

Alternatively, you can use **conda**, since **Anaconda Python** is the default on the DSVM.

```
$ ./conda_env_dsvm.sh
$ source activate flaskweb
$ python --version
Python 3.5.2 :: Anaconda custom (64-bit)
$ python app.py
```

See https://www.anaconda.com

---

## 7. Deploy as a Docker image to a Data Science Virtual Machine (DSVM)

Since both the Azure CLI and Docker are installed on the DSVM, you can also execute
your Docker image, rather than the source code, on the DSVM.

```
$ az --help
$ docker --help

$ sudo docker run -d -e PORT=5000 -p 5000:5000 cjoakim/webapp-docker-python:latest
$ sudo docker ps
$ sudo docker stop -t 1 6a4895321e9e
```

---

## Links

- https://azure.microsoft.com/en-us/develop/python/
- https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-python
- https://docs.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-python-postgresql 
- https://docs.microsoft.com/en-us/azure/app-service/web-sites-python-configure
- https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
- git clone https://github.com/Azure-Samples/flask-postgresql-app
- https://www.anaconda.com
