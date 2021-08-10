### ______________ MARIADB ______________ ###

FROM mariadb:latest as mariadb

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

# get do2unix and curl
RUN apt-get update && apt-get -y install dos2unix curl

# run MariaDB in foreground
CMD ["mysqld", "--character-set-server=utf8mb4", "--collation-server=utf8mb4_unicode_ci", "-uroot"]


### ______________ BASE IMAGE ______________ ###

FROM ubuntu:18.04 as specify_base_ubuntu

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

# Get Ubuntu packages
RUN apt-get update && apt-get -y install \
	unzip curl git sudo

# Clean Up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*




### ______________ SPECIFY 7 ______________ ###

FROM specify_base_ubuntu as specify7

# Get Ubuntu packages
RUN apt-get update && apt-get -y install \
	python3.6 python3.6-dev python-lxml python-pip \
	python3-pip openjdk-11-jre-headless python3-venv \
	default-libmysqlclient-dev apache2 \
	libapache2-mod-python libapache2-mod-wsgi-py3 \
	libssl-dev libsasl2-dev libldap2-dev ghostscript \
	build-essential aptitude dos2unix imagemagick

RUN aptitude install -y nodejs npm libmariadbclient-dev

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

### SPECIFY 7 ###

# copy the config directory for initial build, but it will be overwritten by the (optionally) mounted volume
COPY specify7_config /usr/local/specify_config

# Get Specify 7
RUN cd /usr/local/ \
	&& git clone https://github.com/specify/specify7/
WORKDIR /usr/local/specify7

# convert line endings
RUN dos2unix /usr/local/specify_config/local_specify_settings.py
RUN dos2unix /usr/local/specify_config/local_specifyweb_apache.conf

# link specify7 config file from the mounted config volume
RUN ln -sf /usr/local/specify_config/local_specify_settings.py ./specifyweb/settings/

# install virtual environment
RUN python3.6 -m venv ve \
	&& ve/bin/pip install --no-cache-dir -r requirements.txt

# copy specify6 installation
COPY specify6_thick_client /usr/local/specify6

# as bower command can't be run as root by default, we'll have to set the global options
RUN echo '{ "allow_root": true }' > /root/.bowerrc

# build the web application
RUN make specifyweb/settings/build_version.py specifyweb/settings/secret_key.py frontend

# remove Specify 6 in order to keep the container smaller (it will be mounted via a docker volume)
RUN rm -rf /usr/local/specify6/*

RUN mkdir -p /usr/local/specify_wb_upload/ /var/www/html/specify/specify_depository \
	&& chmod 777 /usr/local/specify_wb_upload/ \
	&& chmod 777 /var/www/html/specify/specify_depository


### APACHE CONFIGURATION ###

# link log files to stdout and stderr
RUN ln -sf /dev/stdout /var/log/apache2/access.log \
    && ln -sf /dev/stderr /var/log/apache2/error.log

# link apache config file from the mounted config volume
RUN rm /etc/apache2/sites-enabled/000-default.conf \
	&& ln -sf /usr/local/specify_config/local_specifyweb_apache.conf /etc/apache2/sites-enabled/

RUN /usr/sbin/a2ensite default-ssl
RUN /usr/sbin/a2enmod ssl
RUN /usr/sbin/a2enmod headers
RUN /usr/sbin/a2dismod python
RUN /usr/sbin/a2enmod wsgi
RUN /usr/sbin/a2enmod cgid

VOLUME [ "/usr/local/specify6" ]
VOLUME [ "/usr/local/specify_config" ]


### WEB ASSET SERVER ###

# Clone repository
RUN cd /usr/local/ \
	&& git clone https://github.com/specify/web-asset-server/

WORKDIR /usr/local/web-asset-server/

# Get ExifRead, Paste and sh
RUN pip install -r requirements.txt

# disable security since container is going to be isolated
RUN sed -i "s/'test_attachment_key'/None/" settings.py

# set default server to 'paste'
RUN sed -i "s/wsgiref/paste/" settings.py

# change port to 8081
RUN sed -i "s/8080/8081/" settings.py

# create a direcory for attachments # TODO: test if this is needed <<<<<<<<<<<<<<<<<
RUN mkdir -p /home/specify/attachments/


CMD /etc/init.d/apache2 start \
	&& python server.py




### ______________ WEB PORTAL ______________ ###

FROM specify_base_ubuntu as webportal

# Get Ubuntu packages
RUN apt-get update && apt-get -y install \
	python make wget lsof default-jre nginx \
	python python-lxml

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*


# Get Web Portal
RUN cd /home/ \
	&& mkdir specify \
	&& cd specify \
	&& git clone https://github.com/specify/webportal-installer/
WORKDIR /home/specify/webportal-installer/
RUN git checkout improve-build


### INSTALL AND CONFIGURE WEB PORTAL ###

# Configure nginx to proxy the Solr requests and serve the static files by copying the provided webportal-nginx.conf to /etc/nginx/sites-available/
RUN install -o root -g root -m644 ./webportal-nginx.conf /etc/nginx/sites-available/

# Disable the default nginx site and enable the portal site:
RUN rm /etc/nginx/sites-enabled/default \
	&& ln -s /etc/nginx/sites-available/webportal-nginx.conf /etc/nginx/sites-enabled/ \
	&& sudo service nginx stop

# Copy the zip files from the Specify Data Export into the webportal-installer/specify_exports
COPY data/export.zip ./specify_exports/

# Build the Solr app
RUN su - root -c "cd /home/specify/webportal-installer/ && make clean-all && make build-all"

# Run Solr in foreground
# Give Solr time to get up and running
# Import .zip file
# Run Nginx in foreground
CMD ./build/bin/solr start -force -p 8983 \
	&& sleep 10 \
	&& curl -v "http://localhost:8983/solr/export/update/csv?commit=true&encapsulator=\"&escape=\&header=true" --data-binary @${LOCATION}build/col/export/PortalFiles/PortalData.csv -H 'Content-type:application/csv' \
	&& nginx -g 'daemon off;'
