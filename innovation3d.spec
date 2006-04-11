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
%if %{with initscript}
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
%endif
BuildRequires:	glut-devel
BuildRequires:	libtiff-devel
BuildRequires:	nurbs++-devel
BuildRequires:	qt-devel
BuildRequires:	xorg-lib-libXmu-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Innovation3D is an Open Source, 3-dimensional modeling program
developed for Linux.

The goal of Innovation3D ( I3D ) is to provide a modeling tool that
allows an artist to utilize a variety of techniques. Polygonal
modeling is currently the focus, but there is some preliminary support
for NURBS curves and surfaces, as well as basic animation.

%description -l pl

%package subpackage
######		Unknown group!
Summary:	-
Summary(pl):	-
Group:		-

%description subpackage

%description subpackage -l pl

%package libs
Summary:	-
Summary(pl):	-
Group:		Libraries

%description libs

%description libs -l pl


%package devel
Summary:	Header files for ... library
Summary(pl):	Pliki nag³ówkowe biblioteki ...
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ... library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl
Statyczna biblioteka ....

%prep
%setup -q
%patch0 -p1

%build
%configure \
--x-libraries=%{_prefix}/X11R6/lib \
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

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
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

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
