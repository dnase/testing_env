# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "dockerdev" do |dockerdev|
    dockerdev.vm.box = "ubuntu/trusty64"
    dockerdev.vm.hostname = "master.vm"
    dockerdev.vm.provision :shell, inline: "/vagrant/files/deps.sh"
    dockerdev.vm.provider "virtualbox" do |v|
      v.memory = 8192
      v.cpus = 4
    end
  end
end
