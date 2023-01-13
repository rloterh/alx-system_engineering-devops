#This Puppet code installs nginx web server
package { 'nginx':
  ensure     => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://github.com/Daniel-bee/alx-system_engineering-devops/tree/main/0x0C-web_server permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
