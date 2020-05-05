# Specify 7 and Web Portal in Docker

Dockerized version of [Specify 7.4.0](https://github.com/specify/specify7) and [Web Portal 2.0](https://github.com/specify/webportal-installer).

- [Installation](#Installation)
- [Upgrade from Specify 7.3.1 to Specify 7.4.0](#upgrade-from-specify-731-to-specify-740)

## Installation

- Install Docker Desktop ([macOS](https://hub.docker.com/editions/community/docker-ce-desktop-mac/), [Linux](https://docs.docker.com/engine/install/ubuntu/), [Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)) and make sure it is running

- Clone this repository.
  ```bash
    git clone https://github.com/specify/specify7-docker.git
  ```

- If you want to use your own database for specify7, replace `mariadb/database.sql` with an export of your database. Be sure to name it `database.sql`

- If you want to use your own data for WebPortal, replace `webportal/export.zip` with your own export file. Be sure to name it `export.zip`. You can use the Specify Data Export tool to create a Web Portal export zip file ([see the Specify 6 Data Export documentation](https://www.sustain.specifysoftware.org/wp-content/uploads/2017/03/Using-the-Specify-Web-Portal.pdf))

- Build the Docker image and start the container
  ```bash
    cd specify7-docker
    docker-compose up -d
  ```

  Specify 7 instance should now be available at `http://localhost:8080`.
  
  WebPortal instance should now be available at `http://localhost:80`.
  
  Solr admin panel should now be available at `http://localhost:8983`. You can restrict access to Solr from outside the container by commenting out the `8983:8983` line in `docker-compose.yml`

  You can build containers without Specify7. In such case, you can comment out respected sections for `mariadb` and `specify7` in `docker-compose.yml` as well as the `networks` part
  You can build containers without webportal. In such case, you can comment out the `webportal`section in `docker-compose.yml`

  If you want to run Specify7 with a local SQL server, follow [these instructions](https://github.com/specify/specify7-docker/tree/sp7_only)

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


## Upgrading to newer version of Specify7

In order to run a newer version of Specify7, all you have to do copy the Specify 6 client's `specify.jar` and `config/` folder into `specify7/specify6_thick_client` and make sure the database you want to connect to has been upgraded to the new version.

Then:

- Pull the changes from the GitHub repository:

```bash
  git pull origin master
```

- Destroy the container:

```bash
  docker-compose down
```

## Upgrade from Specify 7.3.1 to Specify 7.4.0

In order to run Specify 7.4.0, all you have to do is replace the Specify 6 client 
(`specify6_thick_client`) with Specify 6.8.00 and make sure the database you
want to connect to has been upgraded to the new version.

Then:

- Pull the changes from the GitHub repository:

```
  git pull origin master
```

- Destroy the container:

```
  docker-compose down
```

- Rebuild the container:

```
  docker-compose up -d --build
```

## TODO

- **[PRIORITY]** Deal with line endings error on Winodws machines

- Right now, Specify7 container has Apache web server. Also, Web Portal contaienr uses nginx. Idealy, there should be a separate container for Nginx and Specify 7 with Web Portal should connect to it

- We can uninstall most packages from Specify7 and Web Portal after the build process is over
