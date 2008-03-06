%define	module	File-Which
%define name	perl-%{module}
%define	version	0.05
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Portable implementation of the `which' utility
Group:		Development/Perl
License:	GPL or Artistic
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/pwhich
%{_mandir}/man1/*
%{_mandir}/man3*/*
%{perl_vendorlib}/File
