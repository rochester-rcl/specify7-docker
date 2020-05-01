FROM ubuntu:18.04

LABEL maintainer="Specify Collections Consortium <github.com/specify>"

# Get Ubuntu packages
RUN apt-get update && apt-get -y install \
	python make unzip curl python-lxml wget \
	git sudo default-jre nginx lsof

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


### INSTALL AND CONFIGURE WEBPORTAL ###

# Configure nginx to proxy the Solr requests and serve the static files by copying the provided webportal-nginx.conf to /etc/nginx/sites-available/
RUN install -o root -g root -m644 ${LOCATION}webportal-nginx.conf /etc/nginx/sites-available/

# Disable the default nginx site and enable the portal site:
RUN rm /etc/nginx/sites-enabled/default && \
	ln -s /etc/nginx/sites-available/webportal-nginx.conf /etc/nginx/sites-enabled/ && \
	sudo service nginx stop

# Copy the zip files from the Specify Data Export into the webportal-installer/specify_exports
COPY export.zip ${LOCATION}specify_exports/

# Build the Solr app
RUN su - root -c "cd ${LOCATION} &&  make"

#Start the service
RUN ${LOCATION}/build/bin/solr start -force
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

#Load the Specify data into Solr
#RUN cd ${LOCATION} && \
#	#make load-data
#	curl "http://localhost:8983/solr/export/update/csv?commit=true&encapsulator=\"&escape=\&header=true" \
#			--data-binary @export/PortalFiles/PortalData.csv \
#			-H 'Content-type:application/csv' ;


#RUN mkdir ./solr-7.5.0/server/solr/export && \
#    cp -r ./build/cores/export/core/* ./solr-7.5.0/server/solr/export && \
#    cp ./build/cores/export/web.xml ./solr-7.5.0/server/solr-webapp/webapp/WEB-INF/web.xml 

#RUN ${LOCATION}solr-7.5.0/bin/solr start -force

#RUN curl 'http://localhost:8983/solr/export/update/csv?commit=true&encapsulator="&escape=\&header=true' --data-binary @/usr/local/webportal-installer/build/cores/export/PortalFiles/PortalData.csv -H 'Content-type:application/csv'

#EXPOSE 8080

# CMD ["/usr/local/bin/apache2-foreground", "-D", "FOREGROUND"]
