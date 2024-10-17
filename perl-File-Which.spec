%define	modname	File-Which
%define	modver	1.27

Summary:	Portable implementation of the `which' utility
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/File::Which
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(Env)

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
%autosetup -n %{modname}-%{modver} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3*/*
