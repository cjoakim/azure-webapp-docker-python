# azure-webapp-docker-python

Azure Web App built with Python and the Flask framework

## Links

- https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-python
- https://docs.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-python-postgresql 
- https://docs.microsoft.com/en-us/azure/app-service/web-sites-python-configure
- https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
- git clone https://github.com/Azure-Samples/flask-postgresql-app

## Azure CLI

See https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest

```
$az login

$ az webapp deployment user set --user-name <username> --password <password>
$ az webapp deployment user set --user-name $AZURE_WEBAPP_DEPLOY_NAME --password $AZURE_WEBAPP_DEPLOY_PASS

$ az webapp deployment user show

$ az webapp list-runtimes


```