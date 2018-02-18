#!/usr/bin/python
import time
import docker
import warnings
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/root/ammsd.out'
        self.stderr_path = '/root/ammsd.log'
        self.pidfile_path =  '/tmp/ammsd.pid'
        self.pidfile_timeout = 5
        self.client = docker.from_env(version="1.18") # specify dockerd version
    def run(self):
        while True:
            ignore_images = ['basebox', 'ubuntu']
            # manage running containers
            time.sleep(10)

warnings.filterwarnings("ignore")
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
