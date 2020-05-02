FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /thumbsupnews

COPY requirements.txt /thumbsupnews

RUN pip install -r /thumbsupnews/requirements.txt

WORKDIR /thumbsupnews


COPY . /thumbsupnews
