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
    local("zip -r release.zip . -x env/\* *.git* .DS_STORE \*.pyc")
    put("release.zip", "/home/stringer/")
    with cd("~"):
        run("rm -rf betfair-tennis-api")
        run("unzip release.zip -d betfair-tennis-api")
        with cd(code_dir):
            run("virtualenv env -p /usr/local/lib/python2.7.11/bin/python")
            run("source env/bin/activate")
            run("cp ~/betfair.pem ~/betfair-tennis-api/config/betfair.pem")
            with source_virtualenv():
                run("pip install -r requirements.txt")
                sudo("sudo stop betfair")
                sudo("sudo start betfair")
