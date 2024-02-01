#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'


# Create necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo echo "Hello, this is a test file" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "/^\tlocation \/ {/a $config" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
