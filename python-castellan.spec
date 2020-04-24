
%global service castellan

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-castellan
Version:        3.0.1
Release:        1%{?dist}
Summary:        Generic Key Manager interface for OpenStack

Group:          Development/Languages
License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/castellan
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  openstack-macros
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-mock
BuildRequires:  python3-testtools
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslotest
BuildRequires:  python3-barbicanclient
BuildRequires:  python3-cryptography
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-requests
BuildRequires:  python3-testrepository

%description
Generic Key Manager interface for OpenStack

%package -n python3-%{service}
Summary:    OpenStack common configuration library
%{?python_provide:%python_provide python3-%{service}}

Requires:       python3-babel >= 2.3.4
Requires:       python3-barbicanclient >= 4.5.2
Requires:       python3-cryptography
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-oslo-config >= 2:6.4.0
Requires:       python3-oslo-context >= 2.19.2
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-pbr
Requires:       python3-requests >= 2.18.0

%description -n python3-%{service}
Generic Key Manager interface for OpenStack

%prep
%autosetup -n castellan-%{upstream_version} -S git
%py_req_cleanup

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root %{buildroot}

%check
PYTHON=python3 OS_TEST_PATH=./castellan/tests/unit python3 setup.py test

%files -n python3-%{service}
%doc README.rst LICENSE
%{python3_sitelib}/castellan
%{python3_sitelib}/castellan-*.egg-info

%changelog
* Fri Apr 24 2020 RDO <dev@lists.rdoproject.org> 3.0.1-1
- Update to 3.0.1

