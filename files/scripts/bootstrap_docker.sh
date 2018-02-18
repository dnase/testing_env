apt-get update
apt-get install -y docker.io python python-pip
docker build -t basebox:latest /vagrant/files/containers/base
pip install docker
pip install python-daemon
cp /vagrant/files/amms/ammsd.py /usr/local/bin/ammsd
cp /vagrant/files/amms/build_images.py /usr/local/bin/build_images
chmod +x /usr/local/bin/ammsd
chmod +x /usr/local/bin/build_images
