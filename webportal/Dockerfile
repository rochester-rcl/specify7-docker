FROM ubuntu:18.04

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

# Get Ubuntu packages
RUN apt-get update && apt-get -y install \
	python make unzip curl python-lxml wget \
	git sudo lsof default-jre nginx

ENV LOCATION /home/specify/webportal-installer/

# Get Web Portal
RUN cd /home/ \
	&& mkdir specify \
	&& cd specify \
	&& git clone https://github.com/specify/webportal-installer/ \
	&& cd ${LOCATION} \
	&& git checkout improve-build

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*


### INSTALL AND CONFIGURE WEB PORTAL ###

# Configure nginx to proxy the Solr requests and serve the static files by copying the provided webportal-nginx.conf to /etc/nginx/sites-available/
RUN install -o root -g root -m644 ${LOCATION}webportal-nginx.conf /etc/nginx/sites-available/

# Disable the default nginx site and enable the portal site:
RUN rm /etc/nginx/sites-enabled/default && \
	ln -s /etc/nginx/sites-available/webportal-nginx.conf /etc/nginx/sites-enabled/ && \
	sudo service nginx stop

# Copy the zip files from the Specify Data Export into the webportal-installer/specify_exports
COPY export.zip ${LOCATION}specify_exports/

# Build the Solr app
RUN su - root -c "cd ${LOCATION} && make"

# Run Solr in foreground
# Give Solr time to get up and running
# Import .zip file
# Run Nginx in foreground
CMD ${LOCATION}/build/bin/solr start -force -p 8983 && \
	sleep 10 && \
	curl -v "http://localhost:8983/solr/export/update/csv?commit=true&encapsulator=\"&escape=\&header=true" --data-binary @/home/specify/webportal-installer/build/cores/export/PortalFiles/PortalData.csv -H 'Content-type:application/csv' && \
	nginx -g 'daemon off;'