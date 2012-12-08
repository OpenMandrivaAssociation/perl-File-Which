%define	upstream_name	 File-Which
%define	upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Portable implementation of the `which' utility
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Script)

BuildArch:	noarch

%description
File::Which was created to be able to get the paths to executable programs on
systems under which the `which' program wasn't implemented in the shell.

File::Which searches the directories of the user's PATH (as returned by
File::Spec->path()), looking for executable files having the name specified as
a parameter to which(). Under Win32 systems, which do not have a notion of
directly executable files, but uses special extensions such as .exe and .bat to
identify them, File::Which takes extra steps to assure that you will find the
correct file (so for example, you might be searching for perl, it'll try
perl.exe, perl.bat, etc.)

These slurp/spew subs work for files, pipes and sockets, and stdio,
pseudo-files, and DATA.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/pwhich
%{_mandir}/man1/*
%{_mandir}/man3*/*
%{perl_vendorlib}/File


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-4mdv2012.0
+ Revision: 765276
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-3
+ Revision: 763769
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-2
+ Revision: 667148
- mass rebuild

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.1
+ Revision: 449777
- update to 1.09

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 443904
- adding missing buildrequires:
- update to 1.08

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 408834
- update to 1.07

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 403181
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.05-3mdv2009.0
+ Revision: 223763
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.05-2mdv2008.1
+ Revision: 180398
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2008.0
+ Revision: 46333
- first mdv release

  + Olivier Thauvin <nanardon@mandriva.org>
    - Create perl-File-Which

