Name:		python-python-youtube
Version:	0.9.9
Release:	2
Summary:	A Python wrapper around for YouTube Data API
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/python-youtube/
Source0:	python_youtube-0.9.9.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(dataclasses-json)
BuildRequires:	python%{pyver}dist(isodate)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(requests-oauthlib)
BuildArch:	noarch
%description
A Python wrapper around for YouTube Data API.

%files
%{py_sitedir}/*
