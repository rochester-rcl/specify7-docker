FROM ubuntu:18.04

RUN apt-get update && apt-get -y install mariadb-server



### CONFIGURE MARIADB ###

# set root password
# delete anonymous users
# delete default database
# RUN mysql -u root << UPDATE mysql.user SET Password=PASSWORD('root') WHERE User='root'; \
# 	DELETE FROM mysql.user WHERE User=''; \
# 	DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1'); \
# 	DROP DATABASE IF EXISTS test; \
# 	DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%'; \
# 	FLUSH PRIVILEGES;

# RUN mysql -h 127.0.0.1 -P 3306 -u root -p root -e "SET PASSWORD FOR root@localhost = PASSWORD('root')";
# RUN mysql --user=root << DELETE FROM mysql.user WHERE User='';
# RUN mysql --user=root << DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
# RUN mysql --user=root << DROP DATABASE IF EXISTS test;
# RUN mysql --user=root << DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
# RUN mysql --user=root << FLUSH PRIVILEGES;