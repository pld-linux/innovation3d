# TODO: mv SPECS/i3d.spec,v SPECS/innovation3d.spec,v
#
# Conditional build:
%bcond_with	tiff		# build with tiff support
#
Summary:	Innovation3D - 3D modeling program
Summary(pl):	Innovation3D - program do modelowania 3D
Name:		innovation3d
Version:	0.66.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/innovation3d/%{name}_%{version}.orig.tar.gz
# Source0-md5:	815996383f11b2bf79c82252fba04654
Patch0:		http://dl.sourceforge.net/innovation3d/%{name}_0.66.1-2.diff.gz
URL:		http://innovation3d.sourceforge.net/
BuildRequires:	glut-devel
BuildRequires:	libtiff-devel
BuildRequires:	nurbs++-devel
BuildRequires:	qt-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Innovation3D is an Open Source, 3-dimensional modeling program
developed for Linux.

The goal of Innovation3D (I3D) is to provide a modeling tool that
allows an artist to utilize a variety of techniques. Polygonal
modeling is currently the focus, but there is some preliminary support
for NURBS curves and surfaces, as well as basic animation.

%description -l pl
Innovation3D to program do modelowania trójwymiarowego tworzony dla
Linuksa, udostêpniany z otwartymi ¼ród³ami.

Celem Innovation3D (I3D) jest dostarczenie narzêdzia do modelowania
pozwalaj±cego arty¶cie wykorzystywaæ ró¿norodne techniki. G³ównym
elementem jest teraz modelowanie wielok±tami, ale jest pocz±tkowa
obs³uga krzywych i powierzchni NURBS, a tak¿e podstawowej animacji.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{?with_tiff: --with-tiff-prexix=/usr/ } \
	--with-python-version=2.4

#    --with-gl-prefix=PFX     Prefix where OpenGL or Mesa is installed
#    --with-gl-includes=DIR   where the OpenGL or Mesa includes are installed
#    --with-gl-libraries=DIR  where the OpenGL or Mesa libraries are installed
#	--with-glut-prefix=PFX     Prefix where GLUT is installed
#    --with-glut-includes=DIR   where the GLUT includes are installed
#    --with-glut-libraries=DIR  where the GLUT libraries are installed
#    --with-tiff-prefix=PFX     Prefix where libtiff is installed
#  --with-tiff-includes=DIR   where the libtiff includes are installed
#   --with-tiff-libraries=DIR  where the libtiff libraries are installed
#    --with-python-version=VER    The version of Python to use, 1.5 is default
#      --with-python-prefix=PFX    where the root of Python is installed
#       --with-python-includes=DIR  where the Python includes are installed
#   --with-python-libraries=DIR where the Python libraries are installed.
#     --with-dmalloc-cflags=CFLAGS

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
