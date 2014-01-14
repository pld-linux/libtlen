
%define		_snap	20060309

Summary:	Tlen.pl client library
Summary(pl.UTF-8):	Biblioteka kliencka Tlen.pl
Name:		libtlen
Version:	0
Release:	0.%{_snap}.2
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/tleenx/%{name}-%{_snap}.tar.gz
# Source0-md5:	4a49ac97af4c25b6b924fa929c00e278
URL:		http://libtlen.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libtlen is a library providing an API for client programs which want
to use Tlen.pl, an Instant Messanging protocol based on Jabber, but
with some modifications.

%description -l pl.UTF-8
Biblioteka libtlen dostarcza API dla programów klienckich korzystających
z protokołu Tlen.pl który bazuje na Jabber z niewielkimi modyfikacjami.

%package devel
Summary:	Header files for developping programs using libtlen
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki libtlen
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package is required to develop programs that use Tlen.pl
protocol.

%description devel -l pl.UTF-8
Pakiet wymagany przy pisaniu programów korzystających z protokołu
Tlen.pl.

%package static
Summary:	Static version of libtlen library
Summary(pl.UTF-8):	Biblioteka statyczna libtlen
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libtlen library.

%description static -l pl.UTF-8
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
%attr(755,root,root) %ghost %{_libdir}/libtlen.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%{_includedir}/*
%{_libdir}/libtlen.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libtlen.a
