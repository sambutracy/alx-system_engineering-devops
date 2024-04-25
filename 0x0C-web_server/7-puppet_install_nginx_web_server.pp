#!/usr/bin/env bash
# This script sets up a new Ubuntu machine by installing Nginx.
# Nginx will be configured to listen on port 80 and serve a basic "Hello World" page.
#
echo -e "Updating and installing Nginx.\n"
sudo apt-get update -y -qq && \
	 sudo apt-get install nginx -y

echo -e "\nSetting up some minor stuff.\n"

# Start Nginx service
sudo service nginx start

# Allow Nginx through firewall
sudo ufw allow 'Nginx HTTP'

# Grant user ownership of website files for easier editing
sudo chown -R "$USER":"$USER" /var/www/html
sudo chmod -R 755 /var/www

# Backup default index
cp /var/www/html/index.nginx-debian.html /var/www/html/index.nginx-debian.html.bckp

# Create new index
echo -e "Hello World!" > /var/www/html/index.nginx-debian.html

# Set up redirection to a YouTube video for /redirect_me
sudo sed -i '24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default

# Set up a custom 404 page
echo "Ceci n'est pas une page" >> /var/www/html/error_404.html
sudo sed -i '25i\	error_page 404 /error_404.html;' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

echo -e "\nCompleted.\n"

