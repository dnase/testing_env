#!/usr/bin/python
import time
import docker
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/ammsd.pid'
        self.pidfile_timeout = 5
        self.client = docker.from_env(version="1.18") # specify dockerd version
    def run(self):
        while True:
            # read /vagrant/files/data/coind.json
            # act on the data
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
