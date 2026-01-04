#!/bin/bash

echo "Removing old versions"
source uninstall.sh
deactivate || echo "deactivate command ./not found"
rm -rf .venv

echo "Setting up python version"
pyenv local 3.12.7
python --version

echo "Activating venv"
python -m venv .venv
source .venv/bin/activate
which python

echo "Checking application working"
python - <<EOF
from pymongo import MongoClient
print("App is OK and connected to MongoDB")
EOF

echo "Generating files for OpenAPI - Server"
docker run --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/resources/openapi:/local \
  openapitools/openapi-generator-cli generate \
  -i /local/openapi.yaml \
  -g python-fastapi \
  -o /local/app/generated/server_api \
  --additional-properties=packageName=server,pythonPackage=server_api

echo "Generating files for OpenAPI - Client"
docker run --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/resources/openapi:/local \
  openapitools/openapi-generator-cli generate \
  -i /local/openapi.yaml \
  -g python \
  -o /local/app/generated/client_api \
  --additional-properties=packageName=client,pythonPackage=client_api

echo "Generating files for Order Integration - Client"
docker run --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/resources/integration:/local \
  openapitools/openapi-generator-cli generate \
  -i /local/order.yaml \
  -g python \
  -o /local/app/generated/order/client \
  --additional-properties=packageName=client_order,pythonPackage=client_order

echo "Generating files for Payment Integration - Client"
docker run --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/resources/integration:/local \
  openapitools/openapi-generator-cli generate \
  -i /local/payment.yaml \
  -g python \
  -o /local/app/generated/payment/client \
  --additional-properties=packageName=client_payment,pythonPackage=client_payment

echo "Applying changes to the project"
mkdir ./server
cp -r resources/openapi/app/generated/server_api/src/server ./
touch ./server/__init__.py
touch ./server/apis/__init__.py
touch ./server/models/__init__.py

mkdir ./client
cp -r resources/openapi/app/generated/client_api/client ./
touch ./client/__init__.py
touch ./client/api/__init__.py
touch ./client/models/__init__.py

mkdir ./client_order
cp -r resources/integration/app/generated/order/client/client_order ./
touch ./client_order/__init__.py
touch ./client_order/api/__init__.py
touch ./client_order/models/__init__.py

mkdir ./client_payment
cp -r resources/integration/app/generated/payment/client/client_payment ./
touch ./client_payment/__init__.py
touch ./client_payment/api/__init__.py
touch ./client_payment/models/__init__.py

rm -r resources/openapi/app
rm -r resources/integration/app

echo "Installing requirements for python sample application"
pip install -r requirements.txt

echo "OK"

