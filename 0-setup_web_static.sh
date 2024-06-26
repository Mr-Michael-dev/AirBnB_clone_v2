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
echo "######"
echo "setting up folder structure"
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

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

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership to the user and group recursively
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
echo "##### creating server block #####"
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
sed -i '/^location \/,/^}$/a\n\t location /hbnb_static/ {\n    alias /data/web_static/current/;\n    }' /etc/nginx/sites-available/default

# Restart Nginx to apply the change
echo "###### Restaring Nginx ######"
sudo service nginx restart

sleep 3

echo "###### Nginx restarted. All set ######"

exit 0
