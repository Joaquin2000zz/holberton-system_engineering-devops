# Using Puppet, install puppet-lint 2.5.0

package { 'puppet-lint':
    ensure   => '2.5.0',
    source   => 'https://rubygems.org',
    provider => 'gem'
}
