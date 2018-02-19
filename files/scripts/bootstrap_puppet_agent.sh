wget https://apt.puppetlabs.com/puppet5-release-xenial.deb
dpkg -i puppet5-release-xenial.deb
apt-get update
echo "puppetmaster.amms.net $PUPPETMASTER_IP" >> /etc/hosts
