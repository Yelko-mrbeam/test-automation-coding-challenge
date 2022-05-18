FROM ubuntu:21.10

ENV TZ=Europe/Berlin

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y wget python3-pip python3-dev default-libmysqlclient-dev build-essential python3-pymysql \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "manage.py" ]

HEALTHCHECK  --interval=30s --timeout=3s \
    CMD wget --no-verbose --tries=3 --spider http://localhost:4000/healthcheck/db || exit 1