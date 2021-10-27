FROM python:3.6 AS django
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN apt update
RUN apt -y install libpq-dev
COPY requirements.txt /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt