#!/usr/bin/python
import time
import json
import docker
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/root/ammsd.out'
        self.stderr_path = '/root/ammsd.log'
        self.pidfile_path =  '/tmp/ammsd.pid'
        self.pidfile_timeout = 5
        self.client = docker.from_env()
        self.config_path = '/vagrant/files/data/config.json'
        self.configdata = json.load(open(self.config_path))
    def run(self):
        self.client.login(self.configdata['docker_hub_credentials']['username'], self.configdata['docker_hub_credentials']['password'])
        while True:
            ignore_images = ['basebox', 'ubuntu']
            # manage running containers
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
