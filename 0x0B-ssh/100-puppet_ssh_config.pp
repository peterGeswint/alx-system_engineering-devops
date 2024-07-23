#!/usr/bin/env bash
# make changes to config file using puppet.

file{ '/etc/ssh/ssh_config':
  ensure => 'present',
}

file_line { 'Turn off password auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
  replace => 'true',
}

file_line { 'Use a Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/config',
  math   => '^IdentityFile',
}