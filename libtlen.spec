Summary:	Tlen.pl client library
Summary(pl):	Biblioteka kliecka Tlen.pl
Name:		libTlen
Version:	0.1pre
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://glims.w-s.pl/snapshots/%{name}-%{version}.tar.bz2
URL:		http://glims.w-s.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++-devel
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

%prep
%setup -q

%build
aclocal
autoconf
autoheader
automake -a -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install
install src/libtlen.a $RPM_BUILD_ROOT%{_libdir}

gzip -9nf README ChangeLog NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*
