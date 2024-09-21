FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install -y libpq-dev gcc

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 \
#   libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 \
#   fonts-liberation libappindicator3-1 libnss3 lsb-release xdg-utils

COPY . /app

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
