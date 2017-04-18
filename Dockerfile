FROM node:latest
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y python-pip python-dev
RUN npm install -g less
ENV PATH /usr/local/bin/lessc:$PATH
RUN mkdir /code
WORKDIR /code
ADD libraries.txt /code/
RUN pip install -r libraries.txt
ADD . /code/
