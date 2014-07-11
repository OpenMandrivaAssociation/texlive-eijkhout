# revision 15878
# category Package
# catalog-ctan /macros/generic/eijkhout
# catalog-date 2009-01-21 09:11:46 +0100
# catalog-license collection
# catalog-version undef
Name:		texlive-eijkhout
Version:	20090121
Release:	8
Summary:	Victor Eijkhout's packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/eijkhout
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eijkhout.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090121-2
+ Revision: 751389
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090121-1
+ Revision: 718316
- texlive-eijkhout
- texlive-eijkhout
- texlive-eijkhout
- texlive-eijkhout

