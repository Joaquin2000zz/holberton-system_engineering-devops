# Using Puppet, create a file in /tmp

node default {
    file { 'school' :
        ensure  => 'present',
        path    => '/etc/ssh/ssh_config',
        mode    => '0744',
        owner   => 'www-data',
        group   => 'www-data',
        content => 'Host *\nPasswordAuthentication no\nIdentityFile ~/.ssh/school',
    }
}
