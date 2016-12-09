Name:           git-publish
Version:        1.1
Release:        1%{?dist}
Summary:        Prepare and store patch revisions as git tags
License:        MIT
URL:            https://github.com/stefanha/git-publish
Source0:        https://github.com/stefanha/git-publish/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python2 >= 2.7
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
%build
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
* Fri Dec 9 2016 Stefan Hajnoczi <stefanha@gmail.com> - 1.1-1
- git-publish 1.1
