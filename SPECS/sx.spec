%define debug_package %{nil}

%global gh_user v-byte-cpu

Name:           sx
Version:        0.5.0
Release:        1%{?dist}
Summary:        Fast, modern, easy-to-use network scanner
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/sx/archive/refs/heads/master.zip
BuildRequires:  golang libpcap-devel
Requires:       libpcap

%description
sx is the command-line network scanner designed to follow the UNIX philosophy.

The goal of this project is to create the fastest network scanner with clean and simple code.

%prep
%setup -q -n %{name}-master

%build
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> 0.5.0-1
- v0.5.0

* Tue Apr 27 2021 Jamie Curnow <jc@jc21.com> 0.0.1-1
- Initial release. Project is not versioned

