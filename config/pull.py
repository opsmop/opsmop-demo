# example pull configuration for opsmop-pull
#
# usage: opsmop-pull [apply|check] pull_cfg.py

from opsmop.pull.transports.git import GitTransport
from opsmop.pull.callbacks.rest import RestPost
from opsmop.pull.signals.basic import SleepTimer
from opsmop.client.callbacks import CliCallbacks

repo     = "git@github.com:vespene-io/opsmop-demo.git"
filename = "content/hello.py"
post     = "yourhost.example.com/api/opsmop_status"

# if you don't want to have a pull_cfg.py for each policy
# you may also wish to load these from the environment:
#
#     import os
#     repo = os.environ("REPO")
#     filename = os.environ("FILE")
#
# and then execute opsmop-pull as:
#
#     REPO=git@github.com:vespene-io/opsmop-demo.git FILENAME=hello.py opsmop-pull pull.cfg

TRANSPORT = GitTransport(repo=repo, branch="master")

# this basic configuration just pulls a configuration every so many seconds

SIGNALS = [ SleepTimer(seconds=600) ]

# To have 'watch' modes look to a remote source of information to decide when to pull from transports:
# SIGNALS = [ RabbitMq(server="127.0.0.1", queue="notify") ]

CLI_CALLBACKS = [ CliCallbacks() ]

PULL_CALLBACKS = [ RestPost(post) ]

# whether a pull should be attempted immediately on startup instead of waiting for the first signal

IMMEDIATE=True



