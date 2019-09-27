# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global service castellan

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-castellan
Version:        1.3.1
Release:        2%{?dist}
Summary:        Generic Key Manager interface for OpenStack

Group:          Development/Languages
License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/castellan
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  openstack-macros
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-six
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-oslo-config
BuildRequires:  python%{pyver}-oslo-log
BuildRequires:  python%{pyver}-oslo-utils
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-barbicanclient
BuildRequires:  python%{pyver}-cryptography
BuildRequires:  python%{pyver}-keystoneauth1
BuildRequires:  python%{pyver}-requests
BuildRequires:  python%{pyver}-testrepository

%description
Generic Key Manager interface for OpenStack

%package -n python%{pyver}-%{service}
Summary:    OpenStack common configuration library
%{?python_provide:%python_provide python%{pyver}-%{service}}

Requires:       python%{pyver}-babel >= 2.3.4
Requires:       python%{pyver}-barbicanclient >= 4.5.2
Requires:       python%{pyver}-cryptography
Requires:       python%{pyver}-keystoneauth1 >= 3.4.0
Requires:       python%{pyver}-six
Requires:       python%{pyver}-oslo-config >= 2:6.4.0
Requires:       python%{pyver}-oslo-context >= 2.19.2
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-log >= 3.36.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-stevedore >= 1.20.0
Requires:       python%{pyver}-pbr
Requires:       python%{pyver}-requests >= 2.14.2

%description -n python%{pyver}-%{service}
Generic Key Manager interface for OpenStack

%prep
%autosetup -n castellan-%{upstream_version} -S git
%py_req_cleanup

%build
%{pyver_bin} setup.py build

%install
%{pyver_bin} setup.py install --skip-build --root %{buildroot}

%check
PYTHON=python%{pyver} OS_TEST_PATH=./castellan/tests/unit %{pyver_bin} setup.py test

%files -n python%{pyver}-%{service}
%doc README.rst LICENSE
%{pyver_sitelib}/castellan
%{pyver_sitelib}/castellan-*.egg-info

%changelog
* Thu Sep 19 2019 RDO <dev@lists.rdoproject.org> 1.3.1-2
- Update to 1.3.1


