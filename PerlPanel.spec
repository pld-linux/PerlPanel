Summary:	Panel program written in Perl
Summary(pl):	Panel napisany w Perlu
Name:		PerlPanel
Version:	0.1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://jodrell.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	2b0724b09c0f332a24c509adad3ae791
Patch0:		%{name}-DESTDIR.patch
URL:		http://jodrell.net/projects/perlpanel/
BuildRequires:	perl-tools-pod
Requires:	perl-Gnome2-Wnck
Requires:	perl-Gtk2
Requires:	perl-XML-Simple
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PerlPanel is an attempt to build a useable, lean panel program (like
GNOME's gnome-panel and KDE's Kicker) in Perl, using Gtk2.

%description -l pl
PerlPanel jest prób± stworzenia ³atwego w u¿yciu, lekkiego panela
(podobnego do panela GNOME i Kickera z KDE) w Perlu, przy u¿yciu Gtk2.

%prep
%setup -q
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/perlpanel
%{_pixmapsdir}/*
%{_mandir}/man1/*
