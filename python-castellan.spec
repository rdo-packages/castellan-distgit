%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-castellan
Version:        XXX
Release:        XXX
Summary:        Generic Key Manager interface for OpenStack

Group:          Development/Languages
License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/castellan
Source0:        https://tarballs.openstack.org/castellan/castellan-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
BuildRequires:  python2-mock
BuildRequires:  python2-six
BuildRequires:  python2-testtools
BuildRequires:  python2-oslo-config
BuildRequires:  python2-oslo-log
BuildRequires:  python2-oslo-utils
BuildRequires:  python2-oslotest
BuildRequires:  python2-barbicanclient
BuildRequires:  python2-cryptography
BuildRequires:  python2-keystoneauth1
BuildRequires:  python2-stestr

Requires:       python2-babel >= 2.3.4
Requires:       python2-barbicanclient >= 4.0.0
Requires:       python2-cryptography
Requires:       python2-keystoneauth1 >= 3.3.0
Requires:       python2-six
Requires:       python2-oslo-config >= 2:5.1.0
Requires:       python2-oslo-context >= 2.19.2
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-log >= 3.36.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-stevedore >= 1.20.0
Requires:       python2-pbr

%description
Generic Key Manager interface for OpenStack

%package -n python2-castellan
Summary:    OpenStack common configuration library
%{?python_provide:%python_provide python2-castellan}
Provides:   python-castellan = %{upstream_version}

%description -n python2-castellan
Generic Key Manager interface for OpenStack

%if 0%{?with_python3}
%package -n python3-castellan
Summary:        Generic Key Manager interface for OpenStack
Group:          Development/Libraries

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-mock
BuildRequires:  python3-six
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslotest
BuildRequires:  python3-barbicanclient
BuildRequires:  python3-cryptography
BuildRequires:  python3-keystoneauth1

Requires:       python3-six
Requires:       python3-pbr
Requires:       python3-babel >= 2.3.4
Requires:       python3-barbicanclient >= 4.0.0
Requires:       python3-cryptography
Requires:       python3-keystoneauth1 >= 3.3.0
Requires:       python3-oslo-config >= 2:5.1.0
Requires:       python3-oslo-context >= 2.19.2
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-stevedore >= 1.20.0


%description -n python3-castellan
Generic Key Manager interface for OpenStack
%endif

%prep
%setup -q -n castellan-%{upstream_version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
%endif

%py2_install

%check
%if 0%{?with_python3}
OS_TEST_PATH=./castellan/tests/unit %{__python3} setup.py test
%endif
OS_TEST_PATH=./castellan/tests/unit %{__python2} setup.py test

%files -n python2-castellan
%doc README.rst LICENSE
%{python2_sitelib}/castellan
%{python2_sitelib}/castellan-*.egg-info

%if 0%{?with_python3}
%files -n python3-castellan
%doc README.rst LICENSE
%{python3_sitelib}/castellan
%{python3_sitelib}/castellan-*.egg-info
%endif

%changelog
