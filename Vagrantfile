# -*- mode: ruby -*-
# vi: set ft=ruby :

access_key_id = "YOUR KEY"
secret_access_key = "YOUR SECRET KEY"
session_token = "SESSION TOKEN"
keypair_name = "KEYPAIR NAME"
private_key_path = "PATH TO YOUR PRIVATE KEY"

Vagrant.configure("2") do |config|

  # coin daemon server
  config.vm.define "containerhost" do |vbox|
    # general config
    vbox.vm.box = "xcoo/trusty64"
    vbox.vm.hostname = "containerhost.vm"
    vbox.vm.provision :shell, inline: "/vagrant/files/scripts/bootstrap_docker.sh"
    # virtualbox config
    vbox.vm.provider "virtualbox" do |v|
      v.memory = 8192
      v.cpus = 4
    end
    # AWS config
    config.vm.provider :aws do |aws, override|
      aws.access_key_id = access_key_id
      aws.secret_access_key = secret_access_key
      aws.session_token = session_token
      aws.keypair_name = keypair_name
      aws.ami = "ami-99aa41e3"
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = private_key_path
    end
  end
=begin
  # database server
  config.vm.define "databasehost" do |vbox|
    # general config
    vbox.vm.box = "xcoo/trusty64"
    vbox.vm.hostname = "databasehost.vm"
    vbox.vm.provision :shell, inline: "/vagrant/files/scripts/bootstrap_database.sh"
    # virtualbox config
    vbox.vm.provider "virtualbox" do |v|
      v.memory = 8192
      v.cpus = 4
    end
    # AWS config
    config.vm.provider :aws do |aws, override|
      aws.access_key_id = access_key_id
      aws.secret_access_key = secret_access_key
      aws.session_token = session_token
      aws.keypair_name = keypair_name
      aws.ami = "ami-99aa41e3"
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = private_key_path
    end
  end
=end
end
