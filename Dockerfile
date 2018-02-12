FROM python:3.6-slim

MAINTAINER Xinyaun Yao <yao.ntno@gmail.com>

WORKDIR /srv
COPY ./requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
ENV PYTHONPATH /srv
