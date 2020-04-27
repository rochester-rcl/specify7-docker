# Specify 7 and Web Portal in Docker

Dockerized version of [Specify 7](https://github.com/specify/specify7) and [Web Portal](https://github.com/specify/webportal-installer).

Supports Specif 7.4.0 and WebPortal 2.0

## Installation

- Clone this repository.
  ```
    git clone https://github.com/specify/specify7-docker.git
  ```

- Build the Docker image and start the container
  ```
    cd specify7-docker
    docker-compose up -d
  ```
  Your Specify 7 and Web Portal instance should now be available at `http://localhost:<port>`.

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