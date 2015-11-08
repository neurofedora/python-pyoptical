%global modname pyoptical

Name:           python-pyoptical
Version:        0.4
Release:        1%{?dist}
Summary:        Pure python interface to OptiCA
License:        MIT
URL:            https://github.com/esc/pyoptical
Source0:	https://github.com/esc/pyoptical/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

%description
Pure python interface to CRS OptiCAL.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  pyserial
%description -n python2-%{modname}
Pure python interface to CRS OptiCAL.

Python 2 version.


%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-pyserial
%description -n python3-%{modname}
Pure python interface to CRS OptiCAL.

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
  for mod in pyoptical
  do
    mv $mod python2-$mod

    sed -i '1s|^.*$|#!/usr/bin/env %{__python2}|' python2-$mod
    for i in $mod $mod-2 $mod-%{python2_version}
    do
      ln -s python2-$mod $i
    done

    cp python2-$mod python3-$mod
    sed -i '1s|^.*$|#!/usr/bin/env %{__python3}|' python3-$mod

    for i in $mod-3 $mod-%{python3_version}
    do
      ln -s python3-$mod $i
    done
  done
popd

%files -n python2-%{modname}
%doc README.rst
%{_bindir}/pyoptical
%{_bindir}/pyoptical-2
%{_bindir}/pyoptical-2.7
%{_bindir}/python2-pyoptical
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%doc README.rst
%{_bindir}/pyoptical-3
%{_bindir}/pyoptical-3.4
%{_bindir}/python3-pyoptical
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Sat Nov  7 2015 Adrian Alves <alvesadrian@fedoraporject.org> - 0.4-1
- Initial build
