%global tl_name eijkhout
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Victor Eijkhouts packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/eijkhout
License:	collection
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eijkhout.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Three unrelated packages: DB_process, to parse and process database
output; CD_labeler, to typeset user text to fit on a CD label; and
repeat, a nestable, generic loop macro.

