#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Box-Parser-C
Summary:	Mail::Box::Parser::C - reading messages from file using C (XS)
Summary(pl):	Mail::Box::Parser::C - czytanie wiadomo¶ci z pliku z u¿yciem C (XS)
Name:		perl-Mail-Box-Parser-C
Version:	3.004
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31f040a91069a10da2e1e2c936baddc8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mail-Box >= 2.032
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mail::Box::Parser::C implements parsing of messages in ANSI C,
using Perl's XS extension facility.

%description -l pl
Modu³ Mail::Box::Parser::C jest implementacj± analizowania wiadomo¶ci
w ANSI C przy u¿yciu perlowego rozszerzenia XS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorarch}/Mail
%dir %{perl_vendorarch}/Mail/Box
%dir %{perl_vendorarch}/Mail/Box/Parser
%{perl_vendorarch}/Mail/Box/Parser/*.pm
%dir %{perl_vendorarch}/auto/Mail
%dir %{perl_vendorarch}/auto/Mail/Box
%dir %{perl_vendorarch}/auto/Mail/Box/Parser
%dir %{perl_vendorarch}/auto/Mail/Box/Parser/C
%attr(755,root,root) %{perl_vendorarch}/auto/Mail/Box/Parser/C/*.so
%{perl_vendorarch}/auto/Mail/Box/Parser/C/*.bs
%{_mandir}/man3/*
