FROM postgis/postgis:16-3.4

RUN apt-get update && apt-get install -y \
    less \
    make \
    vim \
    git \
    gcc \
    postgresql-server-dev-16

RUN cd /tmp \
&& pwd \
&& git clone https://github.com/postgrespro/rum \
&& pwd \

RUN pwd \
&& cd rum \
&& make USE_PGXS=1

RUN cd /tmp/rum \
&& ls \
&& pwd \
&& make USE_PGXS=1 install 

WORKDIR /tmp/postgres

RUN mkdir /data && chown postgres /data

COPY schema.sql /docker-entrypoint-initdb.d/01.sql

