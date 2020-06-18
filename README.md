# Specify 7 and Web Portal in Docker

Dockerized version of [Specify 7.4.0](https://github.com/specify/specify7) and [Web Portal 2.0](https://github.com/specify/webportal-installer).

## Installation

* Install Docker Desktop ([macOS](https://hub.docker.com/editions/community/docker-ce-desktop-mac/), [Linux](https://docs.docker.com/engine/install/ubuntu/), [Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)) and make sure it is running

* Download this repository:
  1. You can either press the button at the top right corner of this page and then press `Download ZIP`, unzip the downloaded file and place it into a convenient location
  ![](https://update.specifysoftware.org/docker/src/download_link.png)
  2. OR install **Git**, open terminal, navigate to a convenient location and run the following command
  ```bash
    git clone https://github.com/specify/specify7-docker.git
  ```

* If you want to use your own database with specify7, replace `data/database.sql` with an export of your database. Be sure to name it `database.sql`. Instructions on how to create a backup of your database can be found [here](https://update.specifysoftware.org/docker/src/Backup_Specify_Database.pdf)

* If you want to use your own data for Web Portal, replace `data/export.zip` with your export file. Be sure to name it `export.zip`. You can use the Specify Data Export tool to create a Web Portal export zip file ([see the Specify 6 Data Export documentation](https://www.sustain.specifysoftware.org/wp-content/uploads/2017/03/Using-the-Specify-Web-Portal.pdf))

* **[For Windows hosts only]** Follow these instructions in order to avoid getting Drive-related error messages:
  1. Press on the arrow-shaped button in your Start Menu
  2. Find the docker logo and click on it
  3. Select `Settings` in the list of options
  4. Press on the `Resources` tab
  5. Press on the `File Sharing` submenu
  6. Select the drive where your `specify7-docker` folder is located (It is drive `C` in most cases)
  7. Press `Apply & Restart` and wait for Docker to fully reboot (as shown by the indicator in the lower-left corner of the window)
  ![Instructions are shown above](https://update.specifysoftware.org/docker/src/docker_settings.png "Follow these instructions in order to avoid getting Drive-related error messages")

* Build the Docker image and start the container:
  1. Open the terminal (or Command Prompt) in the `specify7-docker` folder (use `cd specify7-docker` to open the directory)
  2. Run the `docker-compose up -d` command
  3. The building process can take about 15 minutes

Specify 7 instance should now be available at `http://localhost:8080`. The login for the default database is `demouser` and the password is also `demouser`.

Web Portal instance should be available at `http://localhost:80`.

You can build containers without Specify7. In such a case, you can comment out respected sections for `mariadb` and `specify7` in `docker-compose.yml` as well as the `networks` part.

You can build containers without Web Portal. In such case, you can comment out the `webportal` section in `docker-compose.yml`.

If you want to run Specify7 with a local SQL server, follow [these instructions](https://github.com/specify/specify7-docker/tree/sp7_only)

* To stop the container:
  ```bash
    docker-compose stop
  ```
* To destroy the container:
  ```bash
    docker-compose down
  ```
* To rebuild the container (for example for a new release of Specify 6):
  ```bash
    docker-compose up -d --build
  ```

## How to report problems and get support?
If you have problems with building containers or have any questions, please send an email to [support@specifysoftware.org](mailto:support@specifysoftware.org). It would help us in solving your issues if you were to attach the output of all the commands you run in the terminal/command prompt.

## Upgrading to a newer version of Specify7

To run a newer version of Specify7, all you have to do is copy the new Specify 6 client's `specify.jar` and `config/` folder into `specify6_thick_client` and make sure the database you want to connect to has been upgraded to the new version of Specify.

Then:

* Pull the changes from the GitHub repository:

  ```bash
    git pull origin master
  ```

* Rebuild the container:

  ```
    docker-compose up -d --build
  ```

## Troubleshooting

* If you get the following error: `ERROR: Service 'mariadb' failed to build: Get https://registry-1.docker.io/v2/library/mariadb/manifests/latest: unauthorized: incorrect username or password`, run `docker logout` in the command line

## TODO

* Right now, Specify7 container has an Apache webserver, Web Portal container uses Nginx, and Web Asset Server is running Bottle. Ideally, there should be a separate container for Nginx, and Specify 7, Web Asset Server, and Web Portal should connect to it.

* We can uninstall most packages from Specify7 and Web Portal after the build process is over in order to reduce container size[![analytics](http://www.google-analytics.com/collect?v=1&t=pageview&dl=https%3A%2F%2Fgithub.com%2Fspecify%2Fspecify7-docker&uid=readme&tid=UA-169822764-6)]()
