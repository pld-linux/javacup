Summary:	Java Based Constructor of Useful Parsers
Summary(pl.UTF-8):	Konstruktor użytecznych parserów bazujący na Javie
Name:		javacup
Version:	10k
Release:	1
License:	distributable, see included LICENSE
Group:		Development/Languages/Java
# Source0-md5:	8b11edfec13c590ea443d0f0ae0da479
Source0:	http://www.cs.princeton.edu/~appel/modern/java/CUP/java_cup_v%{version}.tar.gz
Source1:	%{name}.sh
Source2:	%{name}.csh
URL:		http://www.cs.princeton.edu/~appel/modern/java/CUP/
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java

%description
Java(tm) Based Constructor of Useful Parsers (CUP for short) is a
system for generating LALR parsers from simple specifications. It
serves the same role as the widely used program YACC and in fact
offers most of the features of YACC. However, CUP is written in Java,
uses specifications including embedded Java code, and produces parsers
which are implemented in Java.

%description -l pl.UTF-8
Java(tm) Based Constructor of Useful Parsers (w skrócie CUP) jest
systemem do generowania parserów LALR z prostych specyfikacji. Spełnia
taką samą rolę jak często używany program YACC i faktycznie oferuje
większość z jego możliwości. CUP jest napisany w Javie, wykorzystuje
specyfikację załączająca wbudowany kod Javy i tworzy parsery
zaimplementowane w Javie.

%prep
%setup -q -c

%build
javac java_cup/*.java java_cup/runtime/*.java

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javaclassdir}/%{name}/java_cup/runtime,%{_sysconfdir}/profile.d/}
install java_cup/*.class $RPM_BUILD_ROOT%{_javaclassdir}/%{name}/java_cup
install java_cup/runtime/*.class $RPM_BUILD_ROOT%{_javaclassdir}/%{name}/java_cup/runtime
install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README manual.html
%{_javaclassdir}/%{name}/
%attr(755,root,root) /etc/profile.d/*
