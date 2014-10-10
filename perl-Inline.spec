%define modname	Inline
%define modver 0.77

Summary:	Write Perl subroutines in other programming languages


Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/%{modname}/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl-devel
Requires:	perl(Parse::RecDescent)

%description
The Inline module allows you to put source code from other programming
languages directly "inline" in a Perl script or module. The code is
automatically compiled as needed, and then loaded for immediate access
from Perl.

Inline saves you from the hassle of having to write and compile your
own glue code using facilities like XS or SWIG. Simply type the code
where you want it and run your Perl as normal. All the hairy details
are handled for you. The compilation and installation of your code
chunks all happen transparently; all you will notice is the delay of
compilation on the first run.

The Inline code only gets compiled the first time you run it (or
whenever it is modified) so you only take the performance hit
once. Code that is Inlined into distributed modules (like on the CPAN)
will get compiled when the module is installed, so the end user will
never notice the compilation time.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
#%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Inline*
# %{perl_vendorlib}/auto/Inline*
%{_mandir}/man3/*
