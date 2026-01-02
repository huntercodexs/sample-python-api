#!/bin/bash

echo "Removing old versions"
deactivate
rm -rf .venv

echo "Setting up python version"
pyenv local 3.12.7
python --version

echo "Activating venv"
python -m venv .venv
source .venv/bin/activate
which python

echo "Installing requirements for python sample application"
pip install -r requirements.txt

echo "Checking application working"
python - <<EOF
from pymongo import MongoClient
print("App is OK and connected to MongoDB")
EOF

echo "Application is starting"
uvicorn app.main:app --reload

