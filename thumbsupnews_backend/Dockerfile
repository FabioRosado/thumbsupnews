FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /thumbsupnews_backend

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000