%define	modname	Gtk3
%define	modver	0.016

%define	perl_glib_require 1.240

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Perl module for the GTK+-3.x library
License:	LGPLv2+
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{modname}-%{modver}.tar.gz
# helper for exception management:
Patch1:		exceptions.diff
# set up GdkX11:
Patch6:		GdkX11.diff

BuildArch:	noarch

BuildRequires:	perl(Cairo::GObject) >= 1.0.0
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.300.0
BuildRequires:	perl(Glib) >= 1.302.0-6
BuildRequires:	perl(Glib::Object::Introspection) >= 0.9.0
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= %perl_glib_require
BuildRequires:	perl-Glib-Object-Introspection >= 0.002
BuildRequires:	perl-Test-Simple
# for test suite:
#BuildRequires:	x11-server-xvfb
BuildRequires:	typelib(Gtk) = 3.0
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(Gdk) = 3.0
Requires:	typelib(Pango) = 1.0
# For exception handling:
Requires:	perl(Glib) >= 1.302.0-6

%description
This module provides perl access to the GTK+-3.x library.

GTK+ is the GIMP ToolKit, a library for creating graphical user
interfaces for the X Window System.  GTK+ was originally written for the GIMP
(GNU Image Manipulation Program) image processing program, but is now used by
several other programs as well.

%prep
%setup -q -n %{modname}-%{modver}
%apply_patches
rm -f lib/Gtk3.pm.*
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%check
# (TV) Test suite won't work in iurt (not enough stuff configured):
exit 0
xvfb-run %make test

%files
%doc LICENSE META.yml MYMETA.yml NEWS README
%{perl_vendorlib}/%{modname}.pm
%{_mandir}/*/*
