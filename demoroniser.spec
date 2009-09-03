%define	name    demoroniser	
%define	version 20030916 
%define	release	%mkrel 3

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

