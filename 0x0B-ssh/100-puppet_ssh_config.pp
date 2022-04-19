# Using Puppet, create a file in /tmp

node default {
    file { 'school' :
        ensure  => 'present',
        path    => '/etc/ssh/ssh_config',
        mode    => '0744',
        owner   => 'root',
        group   => 'root',
        content => 'Host *\n PasswordAuthentication no\n IdentityFile ~/.ssh/school',
    }
}
