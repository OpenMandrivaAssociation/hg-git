%define name	hg-git
%define version 0.2.2
%define release %mkrel 1

Summary:	Mercurial plugin for communicating with Git servers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Other
Url:		http://hg-git.github.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	mercurial >= 1.3
Requires:	python-dulwich >= 0.6.0
BuildRequires:	python-dulwich >= 0.6.0
%py_requires -d

%description
This is the Hg-Git plugin for Mercurial, adding the ability to push to
and pull from a Git server repository from Mercurial. This means you
can collaborate on Git based projects from Mercurial, or use a Git
server as a collaboration point for a team with developers using both
Git and Mercurial.

%prep
%setup -q

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
cat <<EOF > hg-git.rc
[extensions]
hgext.bookmarks =
hggit = %{py_sitedir}/hggit
EOF

%__install -m 755 -d %{buildroot}%{_sysconfdir}/mercurial/hgrc.d
%__install -m 644 hg-git.rc %{buildroot}%{_sysconfdir}/mercurial/hgrc.d/

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/hg-git.rc
