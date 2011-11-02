Name:		texlive-eijkhout
Version:	20090121
Release:	1
Summary:	Victor Eijkhout's packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/eijkhout
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eijkhout.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Three unrelated packages: - DB_process, to parse and process
database output; - CD_labeler, to typeset user text to fit on a
CD label; and - repeat, a nestable, generic loop macro.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
