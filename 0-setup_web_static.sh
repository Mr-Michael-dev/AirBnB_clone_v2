#!/usr/bin/env bash
# This script sets up a webserver for the deployment of web static files

# check if Nginx is already installed, if not, install
if ! command -v nginx &> /dev/null;
then
	echo "##### Installing Nginx #####"
	sudo apt-get -y update
	sudo apt-get install nginx -y
	ufw allow 'Nginx HTTP'
	echo "Nginx installed successfully"
else
	echo "Nginx is already installed"
fi

# set up folder structure
echo "setting up folder structure"
if [ ! -e "/data/" ]; then
	mkdir /data/
fi

if [ ! -e "/data/webstatic/" ]; then
	mkdir /data/webstatic/
fi

if [ ! -e "/data/webstatic/releases/" ]; then
	mkdir /data/webstatic/releases/
fi

if [ ! -e "/data/webstatic/shared/" ]; then
	mkdir /data/webstatic/shared/
fi

if [ ! -e "/data/webstatic/releases/test/" ]; then
	mkdir /data/webstatic/releases/test/
fi

# create a fake HTML file to text Nginx configuration
cat << EOF | sudo tee /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# create symbolic link between current and /test/ folder
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/current /data/web_static/releases/test/

# give ownership to the user and group recursively
sudo chown -R ubuntu:ubuntu /data/
