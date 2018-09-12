*Tired of manually creating patch series emails?*

git-publish prepares patches and stores them as git tags for future reference. It works with individual patches as well as patch series. Revision numbering is handled automatically.

No constraints are placed on git workflow, both vanilla git commands and custom workflow scripts are compatible with git-publish.

Email sending and pull requests are fully integrated so that publishing patches can be done in a single command.

Hook scripts are invoked during patch preparation so that custom checks or test runs can be automated.

## How to install

Packages are available for:
* [Fedora](https://koji.fedoraproject.org/koji/packageinfo?packageID=25588) - `dnf install git-publish`
* [Debian](https://packages.debian.org/buster/git-publish) and [Ubuntu](https://packages.ubuntu.com/bionic/git-publish) - `apt install git-publish`
* [RHEL and CentOS](https://koji.fedoraproject.org/koji/packageinfo?packageID=25588) via [EPEL](https://fedoraproject.org/wiki/EPEL) - `yum install git-publish`

Run `git-publish --setup` to install the git alias so you can invoke `git publish` instead of `git-publish`.

## How it works

Send the initial patch series email like this:

```$ git publish --to patches@example.org --cc maintainer@example.org```

You will be prompted for a cover letter on a multi-patch series and you will be presented with a chance to review the emails before they are sent.

Sending successive revisions is easy, you don't need to repeat all the details since git-publish stores them for you:

```$ git publish # to send v2, v3, etc```

## Documentation

Read the man page [here](https://github.com/stefanha/git-publish/blob/master/git-publish.pod).

## Get in touch

Please submit pull requests on GitHub (https://github.com/stefanha/git-publish) or email patches to Stefan Hajnoczi <stefanha@gmail.com>.
