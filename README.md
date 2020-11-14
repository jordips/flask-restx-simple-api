# flask-restx-simple-api

A minimal Flask-restx API example using JSON. Dockerfile included to run in K8S/Docker.

## Run simple API in docker

To build and run docker execute:

```
git clone https://github.com/jordips/flask-restx-simple-api.git
cd flask-restx-simple-api
docker build -t flask-restx-simple-api .
docker run -p 80:80
```
Once Docker is running you can access Swagger via http://localhost

## Development environment

### Requirements

To execute the application you need:
- python3
- pip3

### Run application

You should create and activate a python virtual environment before run the application.

To run development environment:
```
git clone https://github.com/jordips/flask-restx-simple-api.git
cd flask-restx-simple-api
pip3 install -r requirements.txt
python3 run.py
```
Now you can access Swagger via http://localhost:5000
