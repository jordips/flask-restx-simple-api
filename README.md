# flask-restx-simple-api

A minimal Flask-restx API example. Dockerfile included to run in K8S/Docker environments.

## Requirements

To execute code you need:
- python3
- pip3

## Run application in docker

To build and run docker execute:

```
git clone https://github.com/jordips/flask-restx-simple-api.git
cd flask-restx-simple-api
docker build -t flask-restx-simple-api .
docker run -p 80:80
```

## Development environment

You should create and activate a python virtual environment before run the application.

To run development environment:
```
git clone https://github.com/jordips/flask-restx-simple-api.git
cd flask-restx-simple-api
pip3 install -r requirements.txt
python3 run.py
```
