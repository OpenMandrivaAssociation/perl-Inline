%define upstream_name Inline
%define upstream_version 0.52

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Write Perl subroutines in other programming languages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Inline/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl-devel
BuildArch:		noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Inline*
%{perl_vendorlib}/auto/Inline*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.470.0-4mdv2012.0
+ Revision: 765367
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.470.0-3
+ Revision: 763869
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.470.0-2
+ Revision: 667219
- mass rebuild

* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.470.0-1
+ Revision: 634686
- update to new version 0.47

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2010.1
+ Revision: 504495
- update to 0.46

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-1mdv2010.0
+ Revision: 407071
- rebuild using %%perl_convert_version

* Sun Nov 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2009.1
+ Revision: 305992
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.44-11mdv2009.0
+ Revision: 223795
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.44-10mdv2008.1
+ Revision: 180415
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 0.44-9mdv2008.0
+ Revision: 19148
- rebuild


* Fri Feb 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.44-8mdk
- Rebuild
- Add tests

* Tue Jan 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.44-7mdk
- Require Parse::RecDescent (for Inline::C)

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.44-6mdk
- Rebuild for new perl

* Mon Aug 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.44-5mdk
- Rebuild for new perl

* Fri Sep 26 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.44-4mdk
- use %%perl_vendorlib

* Thu Aug 14 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.44-3mdk
- rebuild for new perl (test don't all pass, disabling them, seems
  it really does work)

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.44-2mdk
- fix arch
- rebuild for new auto{prov,req}

