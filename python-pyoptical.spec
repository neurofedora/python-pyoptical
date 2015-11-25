### upstream is not providing LICENSE file
### https://github.com/esc/pyoptical/issues/2

%global modname pyoptical

Name:           python-%{modname}
Version:        0.4
Release:        2%{?dist}
Summary:        Pure python interface to OptiCAL
License:        MIT
URL:            https://github.com/esc/pyoptical
Source0:        https://github.com/esc/pyoptical/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  pyserial
Requires: 	pyserial

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-pyserial
Requires:  	python3-pyserial

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
sed -i -e '1d' %{modname}.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

sed -i -e '1s|^.*$|#!%{__python3}|' %{buildroot}%{_bindir}/%{modname}

%files -n python2-%{modname}
%doc README.rst
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%doc README.rst
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Wed Nov 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.4-2
- Install only one file to bindir according to review

* Sat Nov  7 2015 Adrian Alves <alvesadrian@fedoraporject.org> - 0.4-1
- Initial build
