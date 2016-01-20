from fabric.api import *

env.hosts = ["188.166.159.62"]
env.user = "stringer"
env.key_filename = "~/.ssh/digital-ocean-stringer"

def switch_to_virt_env():
    local("source env/bin/activate")


def pip_install():
    local("pip install -r requirements.txt")


def deploy():
    code_dir = "~/betfair-tennis-api"
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:maxfar/betfair-tennis-api.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        switch_to_virt_env()
        pip_install()
