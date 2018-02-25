FROM python:3.6-slim

MAINTAINER Xinyaun Yao <yao.ntno@gmail.com>

RUN apt-get update && apt-get install -y \
    gcc 

WORKDIR /srv
COPY ./requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
ENV AIRFLOW_HOME /srv
