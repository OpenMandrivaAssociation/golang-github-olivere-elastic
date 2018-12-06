# http://github.com/olivere/elastic
%global forgeurl        https://github.com/olivere/elastic
%global goipath         gopkg.in/olivere/elastic.v2
%global commit          3cfe88295d20b6299bd935131fc0fd17316405ad


%gometa -i

Name:           golang-github-olivere-elastic
Version:        2.0.12
Release:        0.9%{?dist}
Summary:        Elasticsearch client for Go
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# ES must run
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS CONTRIBUTING.md README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 2.0.12-0.8.git3cfe882
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.7.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.6.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.5.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.4.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-0.3.git3cfe882
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Jun 02 2016 jchaloup <jchaloup@redhat.com> - 2.0.12-0.2.git3cfe882
- Enable devel and unit-test subpackages for epel7
  related: #1327781

* Fri Apr 15 2016 jchaloup <jchaloup@redhat.com> - 2.0.12-0.1.git3cfe882
- First package for Fedora
  resolves: #1327781
