Summary:	CHM Tools
Summary(pl):	Narzêdzia CHM
Name:		chmtools
Version:	0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.speakeasy.org/~russotto/chm/%{name}.tar.gz
# Source0-md5:	614b91758ddbeb0ab1c4186fdd13d78a
Patch0:		%{name}-types.patch
URL:		http://www.speakeasy.org/~russotto/chm/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CHM Tools package is a set of tools for working with the CHM files,
consisting of a C language library (called "chmlib" too, but different
from chmlib package), a program called 'chmdump' which dumps out the
files in a CHM file and (incomplete) CHM format documentation.

%description -l pl
Pakiet CHM Tools to zbiór narzêdzi do pracy z plikami CHM, sk³adaj±cy
siê z biblioteki w C (o nazwie tak¿e "chmlib", ale innej ni¿ ta z
pakietu chmlib), programu "chmdump" zrzucaj±cego pliki z pliku CHM
oraz (niepe³nej) dokumentacji do formatu CHM.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install chmdump $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc chmformat.html
%attr(755,root,root) %{_bindir}/*
