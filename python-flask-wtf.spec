# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-flask-wtf
Epoch: 100
Version: 1.2.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Form rendering, validation, and CSRF protection for Flask with WTForms
License: BSD-3-Clause
URL: https://github.com/pallets-eco/flask-wtf/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Simple integration of Flask and WTForms, including CSRF, file upload,
and reCAPTCHA.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-Flask-WTF
Summary: Form rendering, validation, and CSRF protection for Flask with WTForms
Requires: python3
Requires: python3-Flask
Requires: python3-itsdangerous
Requires: python3-WTForms
Provides: python3-Flask-WTF = %{epoch}:%{version}-%{release}
Provides: python3dist(Flask-WTF) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-Flask-WTF = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(Flask-WTF) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-Flask-WTF = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(Flask-WTF) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Flask-WTF
Simple integration of Flask and WTForms, including CSRF, file upload, 
and reCAPTCHA.

%files -n python%{python3_version_nodots}-Flask-WTF
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-flask-wtf
Summary: Form rendering, validation, and CSRF protection for Flask with WTForms
Requires: python3
Requires: python3-flask
Requires: python3-itsdangerous
Requires: python3-wtforms
Provides: python3-flask-wtf = %{epoch}:%{version}-%{release}
Provides: python3dist(flask-wtf) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-flask-wtf = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(flask-wtf) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-flask-wtf = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(flask-wtf) = %{epoch}:%{version}-%{release}

%description -n python3-flask-wtf
Simple integration of Flask and WTForms, including CSRF, file upload, 
and reCAPTCHA.

%files -n python3-flask-wtf
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog
