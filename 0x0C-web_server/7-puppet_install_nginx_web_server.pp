nstall and configure Nginx

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Package['nginx'],
}

# Create the root HTML page with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!",
  require => Package['nginx'],
}

# Configure Nginx with a custom configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;
    server_name _;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/;
    }

    error_page 404 /404.html;
}
  ',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a custom 404 error page
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n\'est pas une page",
  require => Package['nginx'],
}

