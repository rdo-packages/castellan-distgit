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

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  python-mock
BuildRequires:  python-six
BuildRequires:  python-testrepository
BuildRequires:  python-testtools
BuildRequires:  python-oslo-config
BuildRequires:  python-oslo-log
BuildRequires:  python-oslo-utils
BuildRequires:  python-oslotest
BuildRequires:  python-barbicanclient
BuildRequires:  python-cryptography
BuildRequires:  python-keystoneauth1

Requires:       python-babel >= 2.3.4
Requires:       python-barbicanclient >= 4.0.0
Requires:       python-cryptography
Requires:       python-keystoneauth1 >= 3.1.0
Requires:       python-six
Requires:       python-oslo-config >= 2:4.0.0
Requires:       python-oslo-context >= 2.14.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-log >= 3.22.0
Requires:       python-oslo-utils >= 3.20.0
Requires:       python-pbr

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
BuildRequires:  python3-testrepository
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
Requires:       python3-keystoneauth1 >= 3.1.0
Requires:       python3-oslo-config >= 2:4.0.0
Requires:       python3-oslo-context >= 2.14.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-log >= 3.22.0
Requires:       python3-oslo-utils >= 3.20.0


%description -n python3-castellan
Generic Key Manager interface for OpenStack
%endif

%prep
%setup -q -n castellan-%{upstream_version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
%endif

%{__python} setup.py install --skip-build --root %{buildroot}

%check
%if 0%{?with_python3}
OS_TEST_PATH=./castellan/tests/unit %{__python3} setup.py test
%endif
OS_TEST_PATH=./castellan/tests/unit %{__python2} setup.py test

%files -n python2-castellan
%doc README.rst LICENSE
%{python_sitelib}/castellan
%{python_sitelib}/castellan-*.egg-info

%if 0%{?with_python3}
%files -n python3-castellan
%doc README.rst LICENSE
%{python3_sitelib}/castellan
%{python3_sitelib}/castellan-*.egg-info
%endif

%changelog

