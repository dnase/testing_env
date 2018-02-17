# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "dockerdev" do |dockerdev|

    #general config
    dockerdev.vm.box = "xcoo/trusty64"
    dockerdev.vm.hostname = "master.vm"
    dockerdev.vm.provision :shell, inline: "/vagrant/files/bootstrap_docker.sh"

    #virtualbox config
    dockerdev.vm.provider "virtualbox" do |v|
      v.memory = 8192
      v.cpus = 4
    end

    # AWS config
    config.vm.provider :aws do |aws, override|
      aws.access_key_id = "YOUR KEY"
      aws.secret_access_key = "YOUR SECRET KEY"
      aws.session_token = "SESSION TOKEN"
      aws.keypair_name = "KEYPAIR NAME"

      aws.ami = "ami-99aa41e3"

      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = "PATH TO YOUR PRIVATE KEY"
    end
  end
end
