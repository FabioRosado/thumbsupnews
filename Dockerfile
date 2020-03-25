FROM python:3.7-slim-buster
<<<<<<< HEAD

=======
>>>>>>> Train classifier for news articles
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
<<<<<<< HEAD

RUN pip install -r /thumbsupnews/requirements.txt

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /thumbsupnews


=======
RUN pip install -r /thumbsupnews/requirements.txt
>>>>>>> Train classifier for news articles
COPY . /thumbsupnews
