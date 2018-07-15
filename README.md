# azure-webapp-docker-python

Azure Web App built with Python and the Flask framework

## What we'll do

1. Configure workstation
1. Develop the app
1. Dockerize the app
1. Deploy as a Docker image to Azure Container Instance
1. Deploy as a Docker image to Azure App Service
1. Deploy as a GitHub repo to a Data Science Virtual Machine with Ansible

## 1. Configure workstation

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

## 2. Develop the app

## 3. Dockerize the app

## 4. Deploy as a Docker image to Azure Container Instance

## 5. Deploy as a Docker image to Azure App Service

## 6. Deploy as a GitHub repo to a Data Science Virtual Machine with Ansible

## Links

- https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-python
- https://docs.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-python-postgresql 
- https://docs.microsoft.com/en-us/azure/app-service/web-sites-python-configure
- https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
- git clone https://github.com/Azure-Samples/flask-postgresql-app

## Azure CLI

See https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest

```
$ az login

$ az webapp deployment user set --user-name <username> --password <password>
$ az webapp deployment user set --user-name $AZURE_WEBAPP_DEPLOY_NAME --password $AZURE_WEBAPP_DEPLOY_PASS

$ az webapp deployment user show

$ az webapp list-runtimes


```