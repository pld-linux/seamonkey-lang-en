Summary:	British resources for SeaMonkey
Summary(pl):	Brytyjskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-en
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.en-GB.langpack.xpi
# Source0-md5:	2ca823bebb31d34c792d6c2ddd614874
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
British resources for SeaMonkey.

%description -l pl
Brytyjskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
install %{SOURCE1} .
./gen-installed-chrome.sh locale bin/chrome/{en-GB,en-GB-unix}.jar > lang-en-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{en-GB,en-GB-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-en-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/en-GB.jar
%{_chromedir}/en-GB-unix.jar
%{_chromedir}/lang-en-installed-chrome.txt
