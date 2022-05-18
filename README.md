## Pre-requisites
Install python3 and virtualenv or docker
## Run
```shell
virtualenv --python=python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py
```
Access at http://localhost:4000/app/en/user/login.html
```
Email: test
Password: test
```
## Build Docker image locally
```shell
docker build -t automation-coding-challenge .
```
```shell
docker run --name coding_challenge -d -p4002:4000 automation-coding-challenge
```
Access at http://localhost:4002/app/en/user/login.html
```
Email: test
Password: test
```
## Run public docker image
```shell
docker pull yelkomrbeam/test-automation-coding-challenge:0.0.1
```
```shell
docker run --name coding_challenge -d -p4002:4000 yelkomrbeam/test-automation-coding-challenge:0.0.1
```
Access at http://localhost:4002/app/en/user/login.html
```
Email: test
Password: test
```