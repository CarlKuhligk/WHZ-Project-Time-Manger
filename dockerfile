FROM python:3-alpine

WORKDIR /usr/src/app

RUN apk update
RUN apk add --no-cache build-base\ 
    mariadb-dev\
    gcc\
    apache2-utils

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ ./app/

ENTRYPOINT [ "python", "./app/main.py" ]

