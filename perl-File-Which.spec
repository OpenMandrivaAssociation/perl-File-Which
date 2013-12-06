%define	modname	File-Which
%define	modver	1.09

Summary:	Portable implementation of the `which' utility
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Script)

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
%setup -qn %{modname}-%{modver}

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
%{perl_vendorlib}/File
%{_mandir}/man1/*
%{_mandir}/man3*/*

