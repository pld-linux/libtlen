
%define		_snap	20031115

Summary:	Tlen.pl client library
Summary(pl):	Biblioteka kliencka Tlen.pl
Name:		libtlen
Version:	0
Release:	0.%{_snap}.1
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://libtlen.eu.org/snapshots/archive/%{name}-%{_snap}.tar.gz
# Source0-md5:	ab879eeab2643153420e38cdb927468e
URL:		http://www.libtlen.eu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libtlen is a library providing an API for client programs which want
to use Tlen.pl, an Instant Messanging protocol based on Jabber, but
with some modifications.

%description -l pl
Biblioteka libtlen dostarcza API dla programów klienckich korzystaj±cych
z protoko³u Tlen.pl który bazuje na Jabber z niewielkimi modyfikacjami.

%package devel
Summary:	Header files for developping programs using libtlen
Summary(pl):	Pliki nag³ówkowe do biblioteki libtlen
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package is required to develop programs that use Tlen.pl
protocol.

%description devel -l pl
Pakiet wymagany przy pisaniu programów korzystaj±cych z protoko³u
Tlen.pl.

%package static
Summary:	Static version of libtlen library
Summary(pl):	Biblioteka statyczna libtlen
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libtlen library.

%description static -l pl
Biblioteka statyczna libtlen.

%prep
%setup -q -n %{name}-%{_snap}

%build

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/TODO
%attr(755,root,root) %{_libdir}/libtlen.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%{_includedir}/*
%{_libdir}/libtlen.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libtlen.a
