%define		snap 20021029
Summary:	Tlen.pl client library
Summary(pl):	Biblioteka kliencka Tlen.pl
Name:		libtlen
Version:	0.1pre
Release:	0.%{snap}
License:	LGPL
Group:		Libraries
Source0:	http://devnull.bydg.pdi.net/libtlen/snapshots/%{name}-%{snap}.tar.gz
Patch0:		libtlen-destdir.patch
URL:		http://devnull.bydg.pdi.net/libtlen/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libTlen is an object-oriented, cross-platform library which provides
handling logic for the Tlen.pl communication protocol. libTlen is
written in clear C++, so it can be compiled on every platform I think,
but I didn't test it.

%description -l pl
libTlen jest zorientowan± obiektowo, wieloplatformow± bibliotek±,
która zapewnia obs³ugê protoko³u Tlen.pl. libTlen jest napisana w
czystym C++, wiêc wydaje mi siê, ¿e mo¿e byæ kompilowana na ka¿dej
platformie, ale nie testowa³em tego.

%package devel
Summary:	Header files for developping programs using libtlen
Summary(pl):	Pliki nag³ówkowe do biblioteki libtlen
Group:		Development/Libraries
Requires:	%{name} = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
Static libtlen library.

%description static -l pl
Biblioteka statyczna libtlen.

%prep
%setup -q -n %{name}-%{snap}
%patch0 -p1

%build
#cp -f /usr/share/automake/missing .
#%{__aclocal}
#%{__autoconf} -I m4
#autoheader
#%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
