%include	/usr/lib/rpm/macros.perl
Summary:	Panel program written in Perl
Summary(pl):	Panel napisany w Perlu
Name:		PerlPanel
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://jodrell.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	f3d48f7f57561fe8f16c486ced358ca7
Patch0:		%{name}-DESTDIR.patch
URL:		http://jodrell.net/projects/perlpanel/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.031
Requires:	perl-Gtk2 >= 1.031
Requires:	perl-XML-Parser
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
%patch0 -p1

%build
%{__make} \
	PREFIX=%{_prefix}
	
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}
	
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog doc/README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/perlpanel
%{_datadir}/perlpanel
%{_pixmapsdir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
