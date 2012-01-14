#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	SVN
%define		pnam	Notify
%include	/usr/lib/rpm/macros.perl
Summary:	SVN::Notify - Subversion activity notification
Name:		perl-SVN-Notify
Version:	2.83
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DW/DWHEELER/SVN-Notify-%{version}.tar.gz
# Source0-md5:	5430a8b268e91c90b74fa3684c899b13
URL:		http://search.cpan.org/dist/SVN-Notify/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.41
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class may be used for sending email messages for Subversion
repository activity.

There are a number of different modes supported, and SVN::Notify is
fully subclassable, to add new functionality, and offers comprehensive
content filtering to easily modify the format of its messages.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%attr(755,root,root) %{_bindir}/svnnotify
%{_mandir}/man1/svnnotify.1p*
%{_mandir}/man3/SVN::Notify*.3pm*
%{perl_vendorlib}/SVN/Notify.pm
%{perl_vendorlib}/SVN/Notify
