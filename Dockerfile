FROM python:3.7-alpine

ENV FLASK_APP=./app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . /app
WORKDIR /app
RUN pip install -r ./app/requirements.txt


CMD ["flask", "run"]
