%define	upstream_name	 File-Which
%define	upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Portable implementation of the `which' utility
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires: perl(Test::Script)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
