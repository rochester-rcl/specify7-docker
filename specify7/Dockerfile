FROM ubuntu:18.04

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

# Get Ubuntu packages
RUN apt-get update && apt-get -y install \
	python-pip python-dev default-libmysqlclient-dev \
	apache2 libapache2-mod-python libapache2-mod-wsgi \
	libssl-dev libsasl2-dev libldap2-dev unzip curl \
	build-essential curl git aptitude python-lxml dos2unix \
	imagemagick ghostscript authbind sudo #bottlepy
RUN aptitude install -y nodejs npm libmariadbclient-dev

# Get Specify 7
RUN cd /usr/local/ \
	&& git clone https://github.com/specify/specify7/

### INSTALL AND CONFIGURE SPECIFY 7 ###

# copy the config directory for initial build, but it will be overwritten by the (optionally) mounted volume
COPY specify7_config /usr/local/specify_config

# convert line endings
RUN dos2unix /usr/local/specify_config/local_specify_settings.py
RUN dos2unix /usr/local/specify_config/local_specifyweb_apache.conf

# link specify7 config file from the mounted config volume
RUN ln -sf /usr/local/specify_config/local_specify_settings.py /usr/local/specify7/specifyweb/settings/

# install virtual environment
RUN cd /usr/local/specify7/ \
	&& pip install virtualenv --no-cache-dir \
	&& virtualenv /usr/local/specify7/ve \
	&& bash -c "source /usr/local/specify7/ve/bin/activate"

# copy specify6 installation
COPY specify6_thick_client /usr/local/specify6

# as bower command can't be run as root by default, we'll have to set the global options
RUN echo '{ "allow_root": true }' > /root/.bowerrc

# build the web application
RUN	cd /usr/local/specify7/ && \
	su - root -c "cd /usr/local/specify7/ && make build"

# remove Specify 6 in order to keep the container smaller (it will be mounted via a docker volume)
RUN rm -rf /usr/local/specify6/*


############################
### APACHE CONFIGURATION ###
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2

# link log files to stdout and stderr
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \
    ln -sf /dev/stderr /var/log/apache2/error.log

# link apache config file from the mounted config volume
RUN rm /etc/apache2/sites-enabled/000-default.conf  && \
	ln -sf /usr/local/specify_config/local_specifyweb_apache.conf /etc/apache2/sites-enabled/

RUN /usr/sbin/a2ensite default-ssl
RUN /usr/sbin/a2enmod ssl
RUN /usr/sbin/a2dismod python
RUN /usr/sbin/a2enmod wsgi
RUN /usr/sbin/a2enmod cgid

VOLUME [ "/usr/local/specify6" ]
VOLUME [ "/usr/local/specify_config" ]


### WEB ASSET SERVER ###

ENV LOCATION /usr/local/web-asset-server/

# Clone repository
RUN cd /usr/local/ \
	&& git clone https://github.com/specify/web-asset-server/

# Get ExifRead, Paste and sh
RUN cd ${LOCATION} && pip install -r requirements.txt

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Configuration and Deployment

# disable security since container is going to be isolated
RUN cd ${LOCATION} && sed -i "s/'test_attachment_key'/None/" settings.py

# set default server to 'paste'
RUN cd ${LOCATION} && sed -i "s/wsgiref/paste/" settings.py

# allow access to port 8080
RUN touch /etc/authbind/byport/8080 && \
	chmod 500 /etc/authbind/byport/8080

#http://localhost:8080/web_asset_store.xml

CMD /etc/init.d/apache2 start && \
	python ${LOCATION}server.py