apt-get update
apt-get install -y docker.io python python-pip
docker build -t basebox:latest /vagrant/files/containers/base
pip install docker==2.7.0
pip install python-daemon
