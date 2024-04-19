# Puppet manifest for a file in /tmp with specific perm, owner, and content

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet\n',
}
