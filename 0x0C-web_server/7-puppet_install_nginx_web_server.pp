# Update the Ubuntu system and install Nginx.
exec { 'update system':
        command => '/usr/bin/apt-get update',
}

# Ensure Nginx package is installed.
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

# Create an HTML index file with "Hello World!" content.
file {'/var/www/html/index.html':
	content => 'Hello World!'
}

# Set up a redirection rule in the Nginx configuration.
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Ensure Nginx service is running.
service {'nginx':
	ensure => running,
	require => Package['nginx']
}

