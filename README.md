# Specify 7 in Docker

Dockerized version of [Specify 7](https://github.com/specify/specify7). The included
[Docker image](https://github.com/specify/specify7-docker/blob/master/specify7/Dockerfile)
is for version 7.4.0 of the software.

Specify 7 is build upon Specify 6, so you need a running instance of Specify 6.

## Installation

- Clone this repository.
  ```bash
    git clone https://github.com/specify/specify7-docker.git
  ```

- Switch to sp7_only branch
  ```bash
    cd specify7-docker
    git checkout sp7_only
  ```

- Copy your Specify 6 client into the `specify7/specify6_thick_client` directory.
Make sure your directory structure looks like in the image below and that there
is no `specify6` (or something like that) subfolder between the
`specify6_thick_client` folder and the `specify.jar` file and the `config`
subfolder.

  ![](./screenshot-specify6-thick-client-directory-structure.png).

- Rename `example.local_specify_settings.py` in `specify7/specify7_config` to
  `local_specify_settings.py`

- Add your database connection details in `local_specify_settings.py`. If you
  want to connect to a local instance of MySQL, use `host.docker.internal` (that
  works for me on Windows; if it doesn't work on your system, check your
  `etc/hosts` file), not `localhost`, as `DATABASE_HOST`.

- Build the Docker image and start the container
  ```bash
    cd specify7-docker
    docker-compose up -d
  ```
  Your Specify 7 instance should now be available at `http://localhost:<port>`.

- To stop the container:
  ```bash
    docker-compose stop
  ```
- To destroy the container:
  ```bash
    docker-compose down
  ```
- To rebuild the container (for example for a new release of Specify 6):
  ```bash
    docker-compose up -d --build
  ```



