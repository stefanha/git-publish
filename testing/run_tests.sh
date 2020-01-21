#!/bin/bash
# Automated test cases for git-publish
#
# Copyright 2019 Red Hat, Inc.
#
# Authors:
#   Eduardo Habkost <ehabkost@redhat.com>
#
# This work is licensed under the MIT License.  Please see the LICENSE file or
# http://opensource.org/licenses/MIT.

set -e

export TESTS_DIR="$(realpath "$(dirname "$0")")"
export RESULTS_DIR="$(mktemp -d)"

GIT_PUBLISH="$1"
if [ -z "$GIT_PUBLISH" ];then
    GIT_PUBLISH="$TESTS_DIR/../git-publish"
fi
export GIT_PUBLISH="$(realpath "$GIT_PUBLISH")"

source "$TESTS_DIR/functions.sh"

setup_path()
{
    export REAL_GIT="$(which git)"
    export PATH="$RESULTS_DIR/bin:$PATH"
    export PYTHONPATH="$TESTS_DIR:$PYTHONPATH"

    # Place fake git on $PATH to ensure we will never run real git commands by accident:
    mkdir -p "$RESULTS_DIR/bin"
    fake_git="$RESULTS_DIR/bin/git"
    cp "$TESTS_DIR/fake_git" "$RESULTS_DIR/bin/git"

    # Make sure our fake git command will appear first
    assert [ "$(which git)" = "$fake_git" ]

    ln -s "$GIT_PUBLISH" "$RESULTS_DIR/bin/git-publish"
    # make sure `git-publish` command will run our copy:
    assert [ "$(which git-publish)" = "$RESULTS_DIR/bin/git-publish" ]
}

# Create fake git repository for testing
create_git_repo()
{
    "$REAL_GIT" init -q
    cat > A <<EOF
    This is a test file

    One line
    Another line
EOF

    cat > B <<EOF
    Second test file
EOF

    "$REAL_GIT" add A B
    "$REAL_GIT" commit -q -m 'Initial commit'

    echo "Additional line" >> B
    "$REAL_GIT" add B
    "$REAL_GIT" commit -q -m 'Second commit'
}

run_test_case()
{
    local test_case="$1"
    local test_name="$(basename "$test_case")"
    export TEST_DIR="$RESULTS_DIR/$test_name"

    mkdir -p "$TEST_DIR"
    export FAKE_GIT_LOG="$TEST_DIR/fake_git.log"
    export FAKE_GIT_COMMAND_LOG="$TEST_DIR/fake_git_commands.log"
    echo -n "Running test case $test_name: "
    if ! "$test_case" > "$TEST_DIR/test_output.log" 2>&1;then
        echo FAILED
        echo "--- Last 10 lines of test output: ---"
        tail -n 10 "$TEST_DIR/test_output.log"
        echo "-------------------------------------"
        echo "Other log files are available at $TEST_DIR" >&2
        exit 1
    fi
    echo OK
}

# override $HOME so that git-config will never read/write ~/.gitconfig
mkdir "$RESULTS_DIR/home"
export HOME="$RESULTS_DIR/home"

SOURCE_DIR="$RESULTS_DIR/source"

# set fake user name and email to make git happy if system values are not set
cat >> "$RESULTS_DIR/home/.gitconfig" <<EOF
[user]
	email = git-publish-tests@example.com
	name = git-publish tests
EOF

setup_path

for t in "$TESTS_DIR"/[0-9]*;do
    mkdir "$SOURCE_DIR"
    cd "$SOURCE_DIR"
    create_git_repo

    run_test_case "$t"

    cd - >/dev/null
    rm -rf "$SOURCE_DIR"
done

# Note that we'll delete the results dir only if all tests passed,
# so failures can be investigated
rm -rf "$RESULTS_DIR"
