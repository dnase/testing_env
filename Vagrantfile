# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'json'

# number of webservers to provision
webservers = 1
# puppet master IP to hardcode into /etc/hosts
puppetserver_internal_ip = '172.31.32.66'
# IP address data
private_ip_data = {}

configuration = JSON.parse(File.read('files/data/config.json'))

Vagrant.configure("2") do |config|
  # puppet master
  config.vm.define "puppetmaster" do |vbox|
    # general config
    vbox.vm.box = "xcoo/xenial64"
    vbox.vm.hostname = "puppetmaster.amms.net"
    # virtualbox config
    vbox.vm.provider "virtualbox" do |v|
      v.memory = 8192
      v.cpus = 4
    end
    # AWS config
    vbox.vm.provider :aws do |aws, override|
      aws.access_key_id = configuration['aws_credentials']['access_key_id']
      aws.secret_access_key = configuration['aws_credentials']['secret_access_key']
      aws.keypair_name = configuration['aws_credentials']['keypair_name']
      aws.private_ip_address = puppetserver_internal_ip
      aws.instance_type = "t2.medium"
      aws.region = "us-east-1"
      aws.region_config "us-east-1", :ami => "ami-b3425cc9"
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = configuration['aws_credentials']['keypath']
    end
    vbox.vm.provision :shell, inline: "chmod +x /vagrant/files/scripts/*.sh"
    #vbox.vm.provision :shell, inline: "PUPPETMASTER_IP=#{puppetserver_internal_ip} /vagrant/files/scripts/bootstrap_puppet.sh"
  end

  # coin daemon server
  config.vm.define "containerhost" do |vbox|
    # general config
    vbox.vm.box = "xcoo/xenial64"
    vbox.vm.hostname = "containerhost.amms.net"
    # virtualbox config
    vbox.vm.provider "virtualbox" do |v|
      v.memory = 8192
      v.cpus = 4
    end
    # AWS config
    vbox.vm.provider :aws do |aws, override|
      aws.access_key_id = configuration['aws_credentials']['access_key_id']
      aws.secret_access_key = configuration['aws_credentials']['secret_access_key']
      aws.keypair_name = configuration['aws_credentials']['keypair_name']
      aws.instance_type = "t2.medium"
      aws.region = "us-east-1"
      aws.region_config "us-east-1", :ami => "ami-b3425cc9"
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = configuration['aws_credentials']['keypath']
    end
    vbox.vm.provision :shell, inline: "chmod +x /vagrant/files/scripts/*.sh"
    vbox.vm.provision :shell, inline: "/vagrant/files/scripts/bootstrap_docker.sh"
    vbox.vm.provision :shell, inline: "PUPPETMASTER_IP=#{puppetserver_internal_ip} /vagrant/files/scripts/bootstrap_puppet.sh"
  end

  # web servers
  (0...webservers).each { |w|
    config.vm.define "webhost#{w}" do |vbox|
      # general config
      vbox.vm.box = "xcoo/xenial64"
      vbox.vm.hostname = "webhost#{w}.amms.net"
      # virtualbox config
      vbox.vm.provider "virtualbox" do |v|
        v.memory = 8192
        v.cpus = 4
      end
      # AWS config
      vbox.vm.provider :aws do |aws, override|
        aws.elb = "webserver"
        aws.access_key_id = configuration['aws_credentials']['access_key_id']
        aws.secret_access_key = configuration['aws_credentials']['secret_access_key']
        aws.keypair_name = configuration['aws_credentials']['keypair_name']
        aws.instance_type = "t2.medium"
        aws.region = "us-east-1"
        aws.region_config "us-east-1", :ami => "ami-63866d19"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = configuration['aws_credentials']['keypath']
      end
      vbox.vm.provision :shell, inline: "chmod +x /vagrant/files/scripts/*.sh"
      vbox.vm.provision :shell, inline: "/vagrant/files/scripts/bootstrap_webapp.sh"
      vbox.vm.provision :shell, inline: "PUPPETMASTER_IP=#{puppetserver_internal_ip} /vagrant/files/scripts/bootstrap_puppet.sh"
    end
  }
  puts private_ip_data.to_s
end
