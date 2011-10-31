Summary:	Innovation3D - 3D modeling program
Summary(pl.UTF-8):	Innovation3D - program do modelowania 3D
Name:		innovation3d
Version:	0.66.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/innovation3d/%{name}_%{version}.orig.tar.gz
# Source0-md5:	815996383f11b2bf79c82252fba04654
Patch0:		http://dl.sourceforge.net/innovation3d/%{name}_0.66.1-2.diff.gz
# Patch0-md5:	16bff5638fa48a201dedaf6d50dcacb7
Patch1:		%{name}-gcc4.patch
URL:		http://innovation3d.sourceforge.net/
BuildRequires:	glut-devel
BuildRequires:	libtiff-devel
BuildRequires:	nurbs++-devel
BuildRequires:	qt-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-ffriend-injection

%description
Innovation3D is an Open Source, 3-dimensional modeling program
developed for Linux.

The goal of Innovation3D (I3D) is to provide a modeling tool that
allows an artist to utilize a variety of techniques. Polygonal
modeling is currently the focus, but there is some preliminary support
for NURBS curves and surfaces, as well as basic animation.

%description -l pl.UTF-8
Innovation3D to program do modelowania trójwymiarowego tworzony dla
Linuksa, udostępniany z otwartymi źródłami.

Celem Innovation3D (I3D) jest dostarczenie narzędzia do modelowania
pozwalającego artyście wykorzystywać różnorodne techniki. Głównym
elementem jest teraz modelowanie wielokątami, ale jest początkowa
obsługa krzywych i powierzchni NURBS, a także podstawowej animacji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-x \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir} \
	--with-nurbs-includes=%{_includedir}/nurbs++ \
	--with-nurbs-libs=%{_libdir} \
	--with-python-version=%{python_version} \
	--with-python-includes=%{_includedir}/python%{python_version} \
	--with-python-libraries=%{_libdir} \
	--with-tiff-includes=%{_includedir} \
	--with-tiff-libraries=%{_libdir} \
	--with-gl-libraries=%{_libdir} \
	--with-glut-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif
