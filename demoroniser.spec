%define	name    demoroniser	
%define	version 20030916 
%define release	5

Summary:	Corrects incompatible HTML generated by Microsoft applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:        Public Domain	
Group:		Text tools
URL:	        http://www.fourmilab.ch/webtools/demoroniser/	
Source0:        http://www.fourmilab.ch/webtools/demoroniser/%{name}.zip
Patch0:		%{name}-perl-path.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:       perl
BuildArch:	noarch

%description
Corrects moronic and gratuitously incompatible HTML generated by 
Microsoft applications.  Also can be useful on just text to get rid of
the "smart quotes" Microsoft applications like to use.

%prep
rm -rf %{buildroot}
%setup -q -c -n %{name}-%{version}
%patch0

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 demoroniser.pl %{buildroot}%{_bindir}/demoroniser
install -m 0644 demoroniser.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc demoroniser.man 
%{_bindir}/demoroniser
%{_mandir}/man1/demoroniser.1*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20030916-4mdv2011.0
+ Revision: 617531
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20030916-3mdv2010.0
+ Revision: 427960
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 20030916-2mdv2009.0
+ Revision: 266559
- rebuild early 2009.0 package (before pixel changes)

* Thu May 15 2008 Adam Williamson <awilliamson@mandriva.org> 20030916-1mdv2009.0
+ Revision: 207712
- bunzip2 patch
- spec clean
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 19980116-5mdv2008.1
+ Revision: 123774
- kill re-definition of %%buildroot on Pixel's request
- import demoroniser


* Thu Jan 05 2006 Lenny Cartier <lenny@mandriva.com> 19980116-5mdk
- rebuild

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 19980116-4mdk
- rebuild

* Wed Jul 17 2002 Lenny Cartier <lenny@mandrakesoft.cml> 19980116-3mdk
- from Ben Reser <ben@reser.org> :
	- More typos.  I need more sleep.

* Fri Jul 12 2002 Ben Reser <ben@reser.org> 19980116-2mdk
- Fix typos in spec file. :( 

*Thu Jul 11 2002 Ben Reser <ben@reser.org> 19980116-1mdk
- First mandrake release


