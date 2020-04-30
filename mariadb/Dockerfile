FROM mariadb:latest
COPY database.sql /docker-entrypoint-initdb.d/

RUN echo "CREATE DATABASE specify;" > /tmp/newfile
RUN echo "USE specify;" >> /tmp/newfile
RUN cat /docker-entrypoint-initdb.d/database.sql >> /tmp/newfile
RUN cp /tmp/newfile /docker-entrypoint-initdb.d/database.sql

RUN head /docker-entrypoint-initdb.d/database.sql