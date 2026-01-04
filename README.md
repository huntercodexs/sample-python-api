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

# Application Programming

...

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


