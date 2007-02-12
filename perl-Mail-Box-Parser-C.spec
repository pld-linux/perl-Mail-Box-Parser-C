#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Box-Parser-C
Summary:	Mail::Box::Parser::C - reading messages from file using C (XS)
Summary(pl.UTF-8):   Mail::Box::Parser::C - czytanie wiadomości z pliku z użyciem C (XS)
Name:		perl-Mail-Box-Parser-C
Version:	3.006
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3dfb3e2729597ae33114250cbce1b884
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mail-Box >= 2.032
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mail::Box::Parser::C implements parsing of messages in ANSI C,
using Perl's XS extension facility.

%description -l pl.UTF-8
Moduł Mail::Box::Parser::C jest implementacją analizowania wiadomości
w ANSI C przy użyciu perlowego rozszerzenia XS.

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
