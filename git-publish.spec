Name:           git-publish
Version:        1.3
Release:        1%{?dist}
Summary:        Prepare and store patch revisions as git tags
License:        MIT
URL:            https://github.com/stefanha/git-publish
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       git-core

%description
git-publish handles repetitive and time-consuming details of managing patch
email submission.  It works with individual patches as well as patch series and
has support for pull request emails.

Each revision is stored as a git tag including the cover letter (if any).  This
makes it easy to refer back to previous revisions of a patch.  Numbering is
handled automatically and the To:/Cc: email addresses are remembered across
revisions to save you retyping them.

Many projects have conventions for submitting patches.  It is possible to
encode them as a .gitpublish file and hooks/ scripts.  This automatically uses
the right settings and can run a coding style checker or linting tools before
emails are sent.

%prep
%autosetup

# Force Python 3 in Fedora
# https://fedoraproject.org/wiki/Packaging:Python#Multiple_Python_Runtimes
%if 0%{?fedora}
sed -i '1c #!/usr/bin/python3' git-publish
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/git-publish/hooks
install -p -m 755 git-publish %{buildroot}%{_bindir}/
install -p -m 644 hooks/pre-publish-send-email.example %{buildroot}%{_datadir}/git-publish/hooks/

%files
%license LICENSE
%doc README.rst
%_bindir/git-publish
%_datadir/git-publish/hooks/pre-publish-send-email.example

%changelog
* Mon Aug 21 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.3-1
- Add 'e' menu command to edit patches
- Add --notes options for git-notes(1) users
- Replace DEBUG with -v/--verbose option
- Fix git_config_with_profile() profile variable lookup
- Fix --pull-request error when remote cannot be determined
- Support worktrees when invoking hooks
- Improve git error handling

* Wed Mar 1 2017 Stefan Hajnoczi <stefanha@gmail.com> - 1.2-1
- Honor git-config(1) pushDefault/pushRemote options
- Display git-send-email(1) CC list before sending
- Fix git-publish --setup when run outside of a git repo

* Fri Dec 9 2016 Stefan Hajnoczi <stefanha@gmail.com> - 1.1-1
- git-publish 1.1
