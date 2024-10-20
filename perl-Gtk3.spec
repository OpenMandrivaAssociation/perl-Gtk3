%define modname Gtk3
%define modver 0.037

%define perl_glib_require 1.240
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Test::Simple\\)

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	3

Summary:	Perl module for the GTK+-3.x library
License:	LGPLv2+
Group:		Development/GNOME and GTK+
Url:		https://gtk2-perl.sf.net/
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
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl-devel
# for test suite:
#BuildRequires:	x11-server-xvfb
BuildRequires:	typelib(Gtk) = 3.0
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(Gdk) = 3.0
Requires:	typelib(GdkX11) = 3.0
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
%setup -qn %{modname}-%{modver}
%autopatch -p1

rm -f lib/Gtk3.pm.*
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build OPTIMIZE="%{optflags}"

%install
%make_install

%files
%doc LICENSE META.yml NEWS README
%{perl_vendorlib}/%{modname}.pm
%{_mandir}/*/*
