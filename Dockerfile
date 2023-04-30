FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update
RUN apt-get install libpq-dev python3-dev -y

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

