FROM python:3.9.5-alpine as base

COPY src/calculator /calculator

WORKDIR /calculator

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT["python"]
