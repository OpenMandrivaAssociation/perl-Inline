%define name perl-Inline
%define realname Inline
%define version 0.44
%define release %mkrel 9

Summary: Write Perl subroutines in other programming languages
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL or Artistic
Group: Development/Perl
Source: %{realname}-%{version}.tar.bz2
URL: http://search.cpan.org/dist/%{realname}/
Patch0: Inline-0.44-fix-underscore-localization.patch
BuildRequires: perl-devel perl-Parse-RecDescent
Requires: perl(Parse::RecDescent)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n Inline-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Inline*
%{perl_vendorlib}/auto/Inline*

%clean
rm -rf $RPM_BUILD_ROOT

