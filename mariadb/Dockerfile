FROM mariadb:latest

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

COPY database.sql /docker-entrypoint-initdb.d/

RUN echo "CREATE DATABASE specify;" > /tmp/newfile
RUN echo "USE specify;" >> /tmp/newfile
RUN cat /docker-entrypoint-initdb.d/database.sql >> /tmp/newfile
RUN cp /tmp/newfile /docker-entrypoint-initdb.d/database.sql