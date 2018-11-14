OpsMop Demo
===========

Demo content for bin/opsmop and (soon) bin/opsmop-pull

First install [OpsMop](https://github.com/vespene-io/opsmop).

Local Mode Usage
================

Check for errors and missing files:

    opsmop validate content/hello.py

Dry-run mode:

    opsmop check content/hello.py

Apply configuration:

    opsmop apply content/hello.py

Pull Mode Usage
===============

Pending Soon!

opsmop-pull is a pluggable system for fetching remote content and running policy, then remoting status remotely.
It is designed for maximum efficiency.

There are actually four types of plugins involved:
    * Transports - where to get the content (Git, s3, etc)
    * Signals - when to decide to get new content (NoSignals, SQS, RabbitMQ, etc)
    * CliCallbacks - format standard output - the default CLI output is fine
    * PullStatusCallbacks - send status to remote systems (RestPost, etc)

To understand the configuration, see this python file:

    cat config/pull.py

Usage is simple.  Here's the single-shot dry-run mode:

    opsmop-pull check config/pull.py

Single-shot apply configuration (cron, etc):

    opsmop-pull apply config/pull.py

Constantly monitor (systemd, etc):

    opsmop-pull watch-check config/pull.py

Constantly apply (systemd, etc):

    opsmop-pull watch-apply config/pull.py

License
=======

OpsMop is Apache 2 Licensed, (C) Michael DeHaan LLC, 2018.

Content in this repository is public domain.





