#!/usr/bin/python
import os
import json
import docker

container_path = '/vagrant/files/containers'
config_path = '/vagrant/files/data/config.json'
configdata = json.load(open(config_path))
client = docker.from_env()
client.login(configdata['docker_hub_credentials']['username'], configdata['docker_hub_credentials']['password'])

# read /vagrant/files/containers
subdirs = [s for s in os.listdir(container_path) if s != 'base']
# build images if necessary
for subdir in subdirs:
    try:
        img = client.images.get("dnase/amms:%s" % subdir)
    except docker.errors.ImageNotFound:
        buildpath = "%s/%s" % (container_path, subdir)
        client.images.build(path=buildpath, tag="dnase/amms:%s" % subdir)
        client.images.push("dnase/amms", subdir)
