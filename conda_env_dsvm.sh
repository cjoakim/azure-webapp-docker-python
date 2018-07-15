#!/bin/bash

# Bash shell script to create the 'flaskweb' conda/python virtual environment in an Azure DSVM.
# Chris Joakim, Microsoft, 2018/07/15

venvname='flaskweb'

echo 'removing conda environment (if present): '$venvname
conda remove --name $venvname --all -y

echo 'creating conda environment: '$venvname
conda create -n $venvname -y
conda info --envs

echo 'activating conda environment: '$venvname
source activate $venvname

# Note: these pip install commands are copy-and-paste to venv.sh
echo 'installing python packages with pip...'

pip install arrow
pip install Flask
pip install Jinja2

echo 'listing the python packages in this conda environment:'
conda list

echo 'done'
