# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network :forwarded_port, guest: 59008, host: 59008, id: "drumpf", auto_correct: true

  config.vm.provider "virtualbox" do |v, override|
      v.customize ["modifyvm", :id, "--memory", 8192]
      v.customize ["modifyvm", :id, "--cpus", 4]
  end

  config.vm.provision :shell, inline: "/vagrant/files/deps.sh"
end
