%define	_lang	en
%define	_reg	GB
%define	_lare	%{_lang}-%{_reg}
Summary:	British resources for SeaMonkey
Summary(pl.UTF-8):	Brytyjskie pliki językowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.1
Release:	1
License:	GPL
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	de036fa5eaf9649197d04f7c5c25cf2c
Source1:	gen-installed-chrome.sh
URL:		http://www.seamonkey-project.org/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
British resources for SeaMonkey.

%description -l pl.UTF-8
Brytyjskie pliki językowe dla SeaMonkeya.

%prep
%setup -q -c
install %{SOURCE1} .
./gen-installed-chrome.sh locale bin/chrome/{%{_lare},%{_lare}-unix}.jar \
	> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{%{_lare},%{_lare}-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	%{_sbindir}/seamonkey-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/seamonkey-chrome+xpcom-generate ] || %{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lare}-unix.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
