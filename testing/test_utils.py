# Python utility functions for test cases
#
# Copyright 2019 Red Hat, Inc.
#
# Authors:
#   Eduardo Habkost <ehabkost@redhat.com>
#
# This work is licensed under the MIT License.  Please see the LICENSE file or
# http://opensource.org/licenses/MIT.

import os
import shlex
import subprocess
from subprocess import DEVNULL, PIPE, STDOUT

def open_test_log(name='test.log', mode='a'):
    """Open test log file.  Defaults to append mode"""
    return open(os.path.join(os.getenv('TEST_DIR'), name), mode)

def git_command_log():
    with open(os.getenv('FAKE_GIT_COMMAND_LOG'), 'r') as f:
        return [shlex.split(l) for l in f.readlines()]

def last_git_command():
    return git_command_log()[-1]

def git_publish_path():
    return os.getenv('GIT_PUBLISH')

def git_publish(args, **kwargs):
    """Helper to run git-publish using subprocess.run()"""
    if isinstance(args, str):
        args = shlex.split(args)
    return subprocess.run([git_publish_path()] + args, **kwargs)
