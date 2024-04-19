# execute a command that kills the killmenow process
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
