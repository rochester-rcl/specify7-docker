FROM mariadb:latest

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

COPY database.sql /docker-entrypoint-initdb.d/

RUN apt-get update && apt-get -y install dos2unix

RUN dos2unix -f /docker-entrypoint-initdb.d/database.sql
RUN echo "CREATE DATABASE specify;" > /tmp/newfile
RUN echo "USE specify;" >> /tmp/newfile
RUN cat /docker-entrypoint-initdb.d/database.sql >> /tmp/newfile
RUN cp /tmp/newfile /docker-entrypoint-initdb.d/database.sql