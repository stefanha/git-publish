#!/bin/bash
# fake_git sanity checks
#
# Copyright 2019 Red Hat, Inc.
#
# Authors:
#   Eduardo Habkost <ehabkost@redhat.com>
#
# This work is licensed under the MIT License.  Please see the LICENSE file or
# http://opensource.org/licenses/MIT.

source "$TESTS_DIR/functions.sh"

# ensure fake_git is refusing to run git-send-email without --dry-run:
if git send-email --quiet --to somebody@example.com HEAD^..HEAD;then
    abort "fake_git send-email without '--dry-run' was supposed to fail"
fi
grep -q 'send-email --quiet --to somebody@example.com' "$FAKE_GIT_COMMAND_LOG" || \
    abort "fake_git didn't log send-email command"

# --dry-run must succeed, though:
if ! git send-email --dry-run --to somebody@example.com HEAD^..HEAD > /dev/null;then
    abort "git send-email --dry-run failed"
fi

# ensure simple git-publish usage is actually using fake_git:
rm -f "$FAKE_GIT_COMMAND_LOG"
echo q | git-publish -b HEAD^ --to somebody@example.com --inspect-emails || :
[ -s "$FAKE_GIT_COMMAND_LOG" ] || \
    abort "git-publish didn't run fake_git"
