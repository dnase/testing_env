#!/usr/bin/python
import os
import docker
import warnings

warnings.filterwarnings("ignore")
container_path = '/vagrant/files/containers'
client = docker.from_env(version="1.18") # specify dockerd version

# read /vagrant/files/containers
subdirs = [s for s in os.listdir(container_path) if s != 'base']
# build images if necessary
for subdir in subdirs:
    if not client.images.list(name=subdir):
        buildpath = "%s/%s" % (container_path, subdir)
        client.images.build(path=buildpath, tag=subdir)
