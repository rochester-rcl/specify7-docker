# Specify 7 and Web Portal in Docker

Dockerized version of [Specify 7](https://github.com/specify/specify7) and [Web Portal](https://github.com/specify/webportal-installer).

Supports Specif 7.4.0 and WebPortal 2.0

## Installation

- Clone this repository.
  ```
    git clone https://github.com/specify/specify7-docker.git
  ```

- If you want to use your own database for specify7, remove the default database from `specify7/put_your_specify_database_here` and put an `.sql` export of your database there

- If you want to use your own data fro WebPortal, remove the defailt `.zip` export from `specify7/put_your_webportal_export_file_here` and put your `.zip` export in there. YOu can use the Specify Data Export tool to create a Web Portal export zip file (see the Specify 6 Data Export documentation)

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