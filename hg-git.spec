Summary:	Mercurial plugin for communicating with Git servers

Name:		hg-git
Version:	0.6.0
Release:	3
Source0:	http://pypi.python.org/packages/source/h/%{name}/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Other
Url:		https://hg-git.github.com/
BuildArch:	noarch
Requires:	mercurial >= 1.3
Requires:	python-dulwich >= 0.8.0
BuildRequires:	python-dulwich >= 0.8.0
BuildRequires:  python-devel

%description
This is the Hg-Git plugin for Mercurial, adding the ability to push to
and pull from a Git server repository from Mercurial. This means you
can collaborate on Git based projects from Mercurial, or use a Git
server as a collaboration point for a team with developers using both
Git and Mercurial.

%prep
%setup -q

%install

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
cat <<EOF > hg-git.rc
[extensions]
hgext.bookmarks =
hggit = %{py_puresitedir}/hggit
EOF

%__install -m 755 -d %{buildroot}%{_sysconfdir}/mercurial/hgrc.d
%__install -m 644 hg-git.rc %{buildroot}%{_sysconfdir}/mercurial/hgrc.d/

%clean

%files
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/hg-git.rc
%{py_puresitedir}/hg_git*
%{py_puresitedir}/hggit*
