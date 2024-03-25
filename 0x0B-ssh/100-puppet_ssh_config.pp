#!/usr/bin/env bash
# Using puppet to make changes to my ssh configuration file
# setting up my client SSH configuration file so that i can
#connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
  ensure  => present,
content => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
