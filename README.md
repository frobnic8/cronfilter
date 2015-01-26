cronfilter
==========
 ____   ___  _____ ____    _   _  ___ _____  __        _____  ____  _  __
|  _ \ / _ \| ____/ ___|  | \ | |/ _ \_   _| \ \      / / _ \|  _ \| |/ /
| | | | | | |  _| \___ \  |  \| | | | || |    \ \ /\ / / | | | |_) | ' /
| |_| | |_| | |___ ___) | | |\  | |_| || |     \ V  V /| |_| |  _ <| . \
|____/ \___/|_____|____/  |_| \_|\___/ |_|      \_/\_/  \___/|_| \_\_|\_\

This is just a prototype of an idea I'm trying out.

Filter a list of dates based on a cron expression.

Installation
------------
The cronfilter tool is now available in a nice wheel package.

If you've never installed python stuff before, these will probably be the
terminal commands you want to run: (This will prompt you for your login
password)

    sudo easy_install pip
    sudo pip install --upgrade setuptools
    sudo pip install git+https://github.com/frobnic8/cronfilter

To test your installation, run:

    cronfilter --help

If you are still having problems, just let me know and I'll help you out.

Usage
-----
cronfilter takes a cron expression and one or more files (or reads from
standard input) and returns any dates that match the cron expression.
A date matches if it would ever be executed by the cron expression.

If no dates match, then 1 is returned as the exit code.

Files
-----
    README.md                   This file
    cronfilter.py               The command line tool/python module
    test_cronfilter.py          Unit tests runnable with the nosetests command
