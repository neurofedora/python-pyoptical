%global modname pyoptical
%global commit 4cdf06ae9679b5ea87450fcbe6a977bc9070531f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-pyoptical
Version:        0.4
Release:        1%{?dist}
Summary:        Pure python interface to OptiCA
License:        MIT
URL:            https://github.com/esc/pyoptical
Source0:	https://github.com/esc/pyoptical/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Pure python interface to CRS OptiCAL

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  pyserial
%description -n python2-%{modname}
Pure python interface to CRS OptiCAL

Python 2 version.


%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-pyserial
%description -n python3-%{modname}
Pure python interface to CRS OptiCAL

Python 3 version.


%prep
%autosetup -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install


%files -n python2-%{modname}
%doc README.rst
%{_bindir}/%{modname}
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%doc README.rst
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Sat Nov  7 2015 Adrian Alves <alvesadrian@fedoraporject.org> - 0.4-1
- Initial build
