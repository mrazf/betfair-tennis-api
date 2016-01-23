from fabric.api import *

env.hosts = ["46.101.87.122"]
env.user = "stringer"
env.key_filename = "~/.ssh/id_rsa.pub"

def switch_to_virt_env():
    run("virtualenv env")
    run("source env/bin/activate")


def pip_install():
    run("pip install -r requirements.txt")


def deploy():
    code_dir = "~/betfair-tennis-api"
    with cd("~"):
        run("rm -rf betfair-tennis-api")
        run("git clone git@github.com:maxfar/betfair-tennis-api.git")
        with cd("code_dir"):
            run("virtualenv env")
            run("source env/bin/activate")
            run("pip install -r requirements.txt")
            run("sudo restart befair")
