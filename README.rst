===========
git-publish
===========
---------------------------------------------
Prepare and store patch revisions as git tags
---------------------------------------------

Overview
========

Preparing patches for email submission is tedious and takes multiple commands.
Revised patches must be labeled with increasing version numbers like v2, v3,
and so on.  Patch series start with a cover letter that contains a changelog
describing the differences between revisions.  All these details are repetitive
and time-consuming to manage manually.

git-publish prepares patches consistently and stores them as git tags for
future reference.  It works with individual patches as well as patch series.
No constraints are placed on git workflow, both vanilla git commands and custom
workflow scripts are compatible with git-publish.  Email sending is fully
integrated so that publishing a new patch revision can be done in a single
command.

Installing git-publish
======================

First, put the git-publish script somewhere and make sure it has execute
permissions::

  $ mv ~/Downloads/git-publish ~/bin/
  $ chmod u+x ~/bin/git-publish

Then run git-publish in setup mode to configure the git alias::

  $ ~/bin/git-publish --setup
  You can now use 'git publish' like a built-in git command.

Storing patch revisions
=======================

To store the first revision of a patch series::

  $ git checkout my-feature
  $ git publish

This creates the my-feature-v1 git tag.  Running git-publish again at a later
point will create tags with incrementing version numbers::

  my-feature-v1
  my-feature-v2
  my-feature-v3
  ...

To refer back to a previous version, simply check out that git tag.  This way a
record is kept of each patch revision that has been published.

Overriding the version number
-----------------------------

The version number can be set manually.  This is handy when starting out with
git-publish on branches that were previously manually versioned::

  $ git checkout my-existing-feature
  $ git publish --number 7

This creates the my-existing-feature-v7 tag.

Overriding the branch name
--------------------------

By default git-publish refuses to create a revision for the 'master' branch.
Usually one works with so-called topic branches, one branch for each feature
under development.  Using the 'master' branch may indicate that one has
forgotten to switch onto the intended topic branch.  It is possible to override
the topic name and even publish on 'master'::

  $ git checkout branch-a
  $ git publish --topic branch-b

This creates branch-b-v1 instead of branch-a-v1 and can be used to skip the
check for 'master'.

Tag messages
============

Tag messages have a summary (or subject line) and a description (or blurb).
When send email integration is used the summary is put into the cover letter
Subject: line while the description is put into the body.

When prompting for tag messages on v2, v3, or other incremental revisions, the
previous revision's tag message is used as the starting point.  This is handy
for updating the existing description and keeping a changelog of the difference
between revisions.

When preparing a single patch, git-publish creates tags without messages by
default.  It can be handy to include a tag message (or cover letter) if there
is more than one patch in a series.  By default a tag message will be prompted
when there are multiple patches.

To insist on creating a tag message::

  $ git publish --message

To refrain from creating a tag message::

  $ git publish --no-message

Setting the base branch
=======================

git-publish detects whether the branch contains a single commit or multiple
commits by comparing against a base branch ('master' by default).  You can
specify the base branch like this::

  $ git publish --base my-parent

Most of the time 'master' works fine.

It is also possible to persist which base branch to use.  This is useful if you
find yourself often specifying a base branch manually.  It can be done globally
for all branches in a reposity or just for a specific branch::

  $ git config git-publish.base origin/master # for all branches
  $ git config branch.foo.gitpublishbase origin/master # for one branch

Send email integration
======================

git-publish can call git-send-email(1) after creating a git tag.  If there is a
tag message it will be used as the cover letter.  Email can be sent like this::

  $ git publish --to patches@example.org \
                --cc alex@example.org --cc bob@example.org

After the git tag has been created as usual, commits on top of the base branch
are sent as the patch series.  The base branch defaults to 'master' and can be
set manually with --base.

The git-send-email(1) aliasesfile feature works since the email addresses are
passed through without interpretation by git-publish.

Patch emails can be manually edited before being sent, these changes only
affect outgoing emails and are not stored permanently::

  $ git publish --to patches@example.org --annotate

Signed-off-by: <self> lines can be applied to patch emails, only outgoing
emails are affected and not the local git commits::

  $ git publish --to patches@example.org --signoff

Sending [RFC] series instead of regular [PATCH] series can be done by
customizing the Subject: line::

  $ git publish --to patches@example.org --subject-prefix RFC

Support
=======

Please report bugs to Stefan Hajnoczi <stefanha@gmail.com>.
