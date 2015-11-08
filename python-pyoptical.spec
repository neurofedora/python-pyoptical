### upstream is not providing LICENSE file
### https://github.com/esc/pyoptical/issues/2

%global modname pyoptical

Name:           python-pyoptical
Version:        0.4
Release:        1%{?dist}
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

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

# Rename binaries
pushd %{buildroot}%{_bindir}
  mv %{modname} python2-%{modname}
  sed -i '1s|^.*$|#!/usr/bin/env %{__python2}|' python2-%{modname}
  for i in %{modname} %{modname}-2 %{modname}-%{python2_version}
    do
      ln -s python2-%{modname} $i
  done

  cp python2-%{modname} python3-%{modname}
  sed -i '1s|^.*$|#!/usr/bin/env %{__python3}|' python3-%{modname}

  for i in %{modname}-3 %{modname}-%{python3_version}
    do
      ln -s python3-%{modname} $i
    done
popd

%files -n python2-%{modname}
%doc README.rst
%{_bindir}/%{modname}
%{_bindir}/pyoptical-2
%{_bindir}/pyoptical-%{python2_version}
%{_bindir}/python2-pyoptical
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%doc README.rst
%{_bindir}/pyoptical-3
%{_bindir}/pyoptical-%{python3_version}
%{_bindir}/python3-pyoptical
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Sat Nov  7 2015 Adrian Alves <alvesadrian@fedoraporject.org> - 0.4-1
- Initial build
