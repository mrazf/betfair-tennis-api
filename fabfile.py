import os
from fabric.api import *
from contextlib import contextmanager

env.hosts = ["46.101.87.122"]
env.user = "stringer"
env.password = os.environ['STRINGER_PASSWORD']
env.key_filename = "~/.ssh/id_rsa.pub"

@contextmanager
def source_virtualenv():
    with prefix('source ' + os.path.join("/home/stringer/betfair-tennis-api/env/bin/activate")):
        yield


def deploy():
    code_dir = "~/betfair-tennis-api"
    with cd("~"):
        run("rm -rf betfair-tennis-api")
        run("git clone git@github.com:maxfar/betfair-tennis-api.git")
        with cd(code_dir):
            run("pwd")
            run("virtualenv env")
            run("source env/bin/activate")
            run("ls")
            run("which python")
            with source_virtualenv():
                run("pip install -r requirements.txt")
                run("sudo restart betfair")
