FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y python3 python3-dev python3-pip \
  && apt-get install -y build-essential autoconf libtool pkg-config python-dev libpq-dev libxml2-dev libxslt1-dev zlib1g-dev  \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /thumbsupnews

COPY requirements.txt /thumbsupnews

RUN pip3 install setuptools --upgrade

RUN pip3 install --upgrade pip wheel

RUN pip3 install -r /thumbsupnews/requirements.txt

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /thumbsupnews/thumbsupnews_backend

COPY . /thumbsupnews
