Name:		texlive-eijkhout
Version:	15878
Release:	1
Summary:	Victor Eijkhout's packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/eijkhout
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eijkhout.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Three unrelated packages: - DB_process, to parse and process
database output; - CD_labeler, to typeset user text to fit on a
CD label; and - repeat, a nestable, generic loop macro.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/eijkhout/CD_labeler.tex
%{_texmfdistdir}/tex/generic/eijkhout/CD_labeler_test.tex
%{_texmfdistdir}/tex/generic/eijkhout/DB_process.tex
%{_texmfdistdir}/tex/generic/eijkhout/repeat.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
