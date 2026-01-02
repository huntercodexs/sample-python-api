# Sample Python API
This is a sample application for python API projects

# Definition

### Details

Python Version: 3.12.7

### About
This project use layers as structure for application folders and concepts, it does not apply clean arch concepts or 
others like SOLID and clean code, patterns, or other concepts from modern and most used in te market.

The only goal for this small repository is just to offer a simple overview and understable code base for learning 
purposes but can be used as a reference for another kind of projects using python.

Weather you are using PyCharm from JetBrains, even CE edition, just click on `Run in Terminal` button to run each piece
of code or script in the "Usage" session.

However, if you are using the terminal to run this sample project use the script below

```text
./run.sh
```

# Usage

1. Update system

```shell
sudo apt update
sudo apt install -y \
  make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev \
  wget curl llvm libncursesw5-dev xz-utils \
  tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

2. Install pyenv (env manager for python)

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

3. Installing pyenv versions

```shell
echo "Installing python versions"
pyenv install 3.8.18
pyenv install 3.9.23
pyenv install 3.10.18
pyenv install 3.12.7
pyenv install 3.14.0b3
echo "Python versions"
pyenv versions
```

4. Application start

```shell
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
```

5. Application access

```
http://127.0.0.1:8000/health
```

# Project Sample structure

```text
├── app
│        ├── api
│        │       ├── __init__.py
│        │       ├── __pycache__
│        │       │       ├── __init__.cpython-312.pyc
│        │       │       └── routes.cpython-312.pyc
│        │       └── routes.py
│        ├── config
│        │       ├── __init__.py
│        │       ├── __pycache__
│        │       │       ├── __init__.cpython-312.pyc
│        │       │       └── settings.cpython-312.pyc
│        │       └── settings.py
│        ├── db
│        │       ├── __init__.py
│        │       ├── mongo.py
│        │       └── __pycache__
│        │           ├── __init__.cpython-312.pyc
│        │           └── mongo.cpython-312.pyc
│        ├── __init__.py
│        ├── main.py
│        ├── models
│        │       ├── __init__.py
│        │       ├── __pycache__
│        │       │       ├── __init__.cpython-312.pyc
│        │       │       └── user_model.cpython-312.pyc
│        │       └── user_model.py
│        ├── __pycache__
│        │       ├── __init__.cpython-312.pyc
│        │       └── main.cpython-312.pyc
│        ├── repository
│        │       ├── __init__.py
│        │       ├── __pycache__
│        │       │       ├── __init__.cpython-312.pyc
│        │       │       └── user_repository.cpython-312.pyc
│        │       └── user_repository.py
│        └── service
│            ├── __init__.py
│            ├── __pycache__
│            │       ├── __init__.cpython-312.pyc
│            │       └── user_service.cpython-312.pyc
│            └── user_service.py
├── README.md
├── requirements.txt
├── sonar-project.properties
└── tests
    ├── __init__.py
    └── test_users_api.py
```
