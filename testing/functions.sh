# Utility functions for test case shell scripts
#
# Copyright 2019 Red Hat, Inc.
#
# Authors:
#   Eduardo Habkost <ehabkost@redhat.com>
#
# This work is licensed under the MIT License.  Please see the LICENSE file or
# http://opensource.org/licenses/MIT.


tail_fake_git_log()
{
    if [ -r "$FAKE_GIT_LOG" ];then
        echo "---- last 5 lines of fake_git log: ----" >&2
        tail -n 5 "$FAKE_GIT_LOG" >&2
        echo "---- end of fake_git log ----" >&2
    fi
}

abort()
{
    echo "TEST FAILURE: $@" >&2
    exit 1
}

assert()
{
    "$@" || abort "Assertion failed: $@"
}

assert_false()
{
    ! "$@" || abort "Assertion failed: ! $@"
}
