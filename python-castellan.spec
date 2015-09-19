# Created by pyp2rpm-2.0.0
%global pypi_name castellan

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Generic Key Manager interface for OpenStack

License:        ASL 2.0
URL:            http://glance.openstack.org
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

Requires:       python-pbr
Requires:       python-babel
Requires:       python-cryptography >= 1.0
Requires:       python-oslo-config
Requires:       python-oslo-context
Requires:       python-oslo-log
Requires:       python-oslo-policy
Requires:       python-oslo-serialization
Requires:       python-oslo-utils
Requires:       python-six >= 1.9.0

%description
Generic Key Manager interface for OpenStack


%package -n     python2-%{pypi_name}
Summary:        Generic Key Manager interface for OpenStack
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Generic Key Manager interface for OpenStack


%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Generic Key Manager interface for OpenStack
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx

# FIXME: some runtime deps have not been ported to python3
Requires:       python3-pbr
Requires:       python3-babel
Requires:       python3-cryptography
Requires:       python3-oslo-config
Requires:       python3-oslo-context
#Requires:       python3-oslo-log
Requires:       python3-oslo-policy
Requires:       python3-oslo-serialization
#Requires:       python3-oslo-utils
Requires:       python3-six

%description -n python3-%{pypi_name}
Generic Key Manager interface for OpenStack
%endif

%package -n python-%{pypi_name}-doc
Summary:        castellan documentation

%description -n python-%{pypi_name}-doc
Documentation for castellan


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif
%{__python2} setup.py install --skip-build --root %{buildroot}


%files -n python2-%{pypi_name}
%license LICENSE
%doc doc/source/readme.rst README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%if 0%{?with_python3}
%files -n python3-%{pypi_name} 
%license LICENSE
%doc doc/source/readme.rst README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif


%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
* Wed Sep 16 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.2.1-1
- Upstream 0.2.1

* Thu Sep 03 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.2.0-1
- Initial package.
