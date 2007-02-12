Summary:	Cinepak codec for XAnim
Summary(pl.UTF-8):   Kodek Cinepak dla XAnima
Name:		xanim-codec-cvid
Version:	2.1
Release:	1
License:	non-distributable, for use with xanim exclusively
Group:		X11/Applications/Graphics
# old dlls at http://xanim.polter.net/dlls/
Source1:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_cvid_2.1_linuxELFx86c6.tgz
# NoSource1-md5:	570c494c66313e6ee4e90fb0337c0c7f
Source2:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_cvid_2.1_linuxELFalphaC6.tgz
# NoSource2-md5:	6f78c562c71b8087b8957fe0884b0e53
Source3:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_cvid_2.1_linuxELFppc.tgz
# NoSource3-md5:	21f515c731b2653d05dca7188ffb1cbd
NoSource:	1
NoSource:	2
NoSource:	3
URL:		http://xanim.polter.net/
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cinepak codec decompression DLL for XAnim.

%description -l pl.UTF-8
Biblioteka do dekompresji kodeka Cinepak dla XAnima.

%prep
%ifarch %{ix86}
%setup -q -c -T -a1
%endif
%ifarch alpha
%setup -q -c -T -a2
%endif
%ifarch ppc
%setup -q -c -T -a3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_cvid_*.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc cvid.readme
%attr(755,root,root) %{_libdir}/xanim/vid_cvid_*.xa
