FROM mariadb:latest

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

# copy database.sql from host
COPY database.sql /docker-entrypoint-initdb.d/

# get do2unix and curl
RUN apt-get update && apt-get -y install dos2unix curl

# download default database from the server if database.sql is empty
RUN [ ! -s "/docker-entrypoint-initdb.d/database.sql" ] && { curl -o /docker-entrypoint-initdb.d/database.sql https://update.specifysoftware.org/docker/database.sql; }

# run dos2unix on the database fie.
RUN dos2unix -f /docker-entrypoint-initdb.d/database.sql

# append database creation code to the .sql file
RUN echo "CREATE DATABASE specify;" > /tmp/newfile
RUN echo "USE specify;" >> /tmp/newfile
RUN cat /docker-entrypoint-initdb.d/database.sql >> /tmp/newfile
RUN cp /tmp/newfile /docker-entrypoint-initdb.d/database.sql