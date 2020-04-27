# Specify 7 in Docker

Dockerized version of [Specify 7](https://github.com/specify/specify7). The included
[Docker image](https://github.com/specify/specify7-docker/blob/master/specify7/Dockerfile)
is for version 7.4.0 of the software.

Specify 7 is build upon Specify 6, so you need a running instance of Specify 6.

## Installation

- Clone this repository.
  ```
    git clone https://github.com/specify/specify7-docker.git
  ```

- Add your database connection details in `local_specify_settings.py`. If you
  want to connect to a local instance of MySQL, use `host.docker.internal` (that
  works for me on Windows; if it doesn't work on your system, check your
  `etc/hosts` file), not `localhost`, as `DATABASE_HOST`.

- Build the Docker image and start the container
  ```
    cd specify7-docker
    docker-compose up -d
  ```
  Your Specify 7 instance should now be available at `http://localhost:<port>`.

- To stop the container:
  ```
    docker-compose stop
  ```
- To destroy the container:
  ```
    docker-compose down
  ```
- To rebuild the container (for example for a new release of Specify 6):
  ```
    docker-compose up -d --build
  ```

## Installing with containerized MariaDB
Please follow official instructions for [setting up a MariaDB Docker container](https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/)

After that, run you mariadb container like this (replace `root` with your desired password and `mariadb` with the name of your container):
```bash
docker container run --network bridge -e MYSQL_ROOT_PASSWORD=root mariadb
`