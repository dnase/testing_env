curl -L -o /root/pe-latest.tar.gz https://pm.puppetlabs.com/cgi-bin/download.cgi?dist=ubuntu&rel=16.04&arch=amd64&ver=latest
cd /root && tar -xvf pe-latest.tar.gz
cd /root/pe-latest && ./puppet-enterprise-installer -c /vagrant/files/data/pe.conf -q
