%define	name    demoroniser	
%define	version 19980116 
%define	release	%mkrel 5

Summary:	Demoroniser corrects incompatible HTML generated by Microsoft applications
Name:		%name
Version:	%version
Release:	%release
License:        Public Domain	
Group:		Text tools
URL:	        http://www.fourmilab.ch/webtools/demoroniser/	
Source0:        http://www.fourmilab.ch/webtools/demoroniser/%{name}-%{version}.tar.bz2
Patch:		%{name}-perl-path.patch.bz2
BuildRoot:	%_tmppath/%name--buildroot
Requires:       perl
BuildArch:	noarch

%description
Corrects moronic and gratuitously incompatible HTML generated by 
Microsoft applications.  Also can be useful on just text to get rid of
the "smart quotes" Microsoft applications like to use.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
%patch

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0755 demoroniser.pl $RPM_BUILD_ROOT%{_bindir}/demoroniser
install -m 0644 demoroniser.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc demoroniser.man 
%{_bindir}/demoroniser
%{_mandir}/man1/demoroniser.1*

