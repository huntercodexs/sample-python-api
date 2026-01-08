# Sample Python API
This is a sample application for python API projects

# Definition

### Details

- Python Version: 3.12.7
- SonarQube 9.9.8

### About

This project use layers as structure for application folders and concepts, it does not apply clean arch concepts or 
others like SOLID and clean code, patterns, or other concepts from modern and most used in te market.

The only goal for this small repository is just to offer a simple overview and understable code base for learning 
purposes but can be used as a reference for another kind of projects using python.

Weather you are using PyCharm from JetBrains, even CE edition, just click on `Run in Terminal` button to run each piece
of code or script in the "Usage" session.

# Pre Requisites

- Update OS System

```shell
sudo apt update
sudo apt install -y \
  make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev \
  wget curl llvm libncursesw5-dev xz-utils \
  tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

- Install pyenv (env manager for python)

```shell
echo "Downloading pyenv"
curl https://pyenv.run | bash

echo "installing pyenv in /home/${USER}/.pyenv/bin"

echo "Configuring pyenv for global use"
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
source ~/.bashrc

echo "Checking pyenv version"
pyenv --version
```

- Installing pyenv versions

```shell
./pyenv.sh
```

# Installing

- OpenAPI (API First) Generate

```shell
./install.sh
```

- Uninstall

```shell
./uninstall.sh
```

- Application Start

```shell
./run.sh
```

- Application access

```
GET http://127.0.0.1:8000/docs
GET http://127.0.0.1:8000/health
POST http://localhost:8000/users {
  "name": "John Smith",
  "email": "john@email.com"
}
```

# Coverage

> Run this command before sonarqube command

```shell
python -m pytest --cov=app --cov-report=xml --cov-report=term-missing
```

# SonarQube 

- Download Scanner

```shell
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
unzip sonar-scanner-cli-*.zip
ln -s sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner /usr/local/bin/sonar
```

- Run Sonar

```shell
sonar -Dsonar.projectKey=sample-python-api -Dsonar.projectName=sample-python-api -Dsonar.profile=Python -Dsonar.host.url=http://localhost:39003 -Dbranch=main -Dsonar.login=sqa_a66f06519751aae50ed44a248a4fdae5ad072f57
```

- Access Sonar Results

http://localhost:39003/dashboard?id=sample-python-api

# Step by Step

- APIFirst

First of all, create the YAML file specification for swagger according to the requirements of your application, for example:

```yaml
openapi: 3.0.3
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    post:
      operationId: createUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      responses:
        '201':
          description: Created
  /users/{id}:
    get:
      operationId: getUser
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
components:
  schemas:
    User:
      type: object
      required: [name, email]
      properties:
        name:
          type: string
        email:
          type: string
```

- Code Generate

Now generate the files using the script install

```shell
./install.sh
```

it is required to generate the configuration in this script before, for example:

```shell
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
```

- Client Implement

You can easily implement the client code generated following the rules below

```text

```

- Server Implement

The server implementation is made doing the following implementation

```python
from server.apis.default_api import BaseDefaultApi
from app.service.user_service import UserService
from server.models.user import User

class UserApiImpl(BaseDefaultApi):

    def __init__(self):
        self.service = UserService()

    async def create_user(
        self,
        user: User,
    ) -> None:
        self.service.create_user(user)

    def get_users(self):
        return self.service.list_users()
```

As you can see the code above implements BaseDefaultApi that was generated before by openapi and has the 
endpoints to implements, for example

```python
async def create_user(
        self,
        user: User,
    ) -> None:
        self.service.create_user(user)
```

- Client Integration Implement

Here we will talk about integration between applications, for example this application needs to integrate with 
payment or order services as it is possible to below


```python
    def create_user_and_order(self, price: str, quantity: str):
        # business logic here

        print(">>>creating user and order for tests")

        try:
            self.order_client.create_order(
                price=price,
                quantity=quantity
            )
        except Exception as e:
            print(e)
```

This code was generated by openapi and it implements the client_order to create an order in this service

This feature needs to configure in the settings.py script the following details

```python
    order_service_url: str = os.getenv("ORDER_SERVICE_URL", "http://localhost:8081")
    payment_service_url: str = os.getenv("PAYMENT_SERVICE_URL", "http://localhost:8082")
```

- Test + Coverage

```shell
python -m pytest --cov=app --cov-report=xml --cov-report=term-missing
```

- SonarQube

```shell
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
unzip sonar-scanner-cli-*.zip
export PATH=$PATH:sonar-scanner-*/bin

sonar-scanner -Dsonar.projectKey=sample-python-api -Dsonar.projectName=sample-python-api -Dsonar.profile=Python -Dsonar.host.url=http://localhost:39003 -Dbranch=main -Dsonar.login=sqa_a66f06519751aae50ed44a248a4fdae5ad072f57

sonar -Dsonar.projectKey=sample-python-api -Dsonar.projectName=sample-python-api -Dsonar.profile=Python -Dsonar.host.url=http://localhost:39003 -Dbranch=main -Dsonar.login=sqa_a66f06519751aae50ed44a248a4fdae5ad072f57
```

- MongoDB


