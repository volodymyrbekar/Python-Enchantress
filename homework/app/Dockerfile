FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip

WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD app.py /app

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
