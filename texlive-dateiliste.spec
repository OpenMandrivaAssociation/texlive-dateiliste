%global tl_name dateiliste
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Extensions of the \listfiles concept
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dateiliste
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dateiliste.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dateiliste.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dateiliste.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a file list (similar to that offered by
\listfiles), neatly laid out as a table. The main document can be
included in the list, and a command is available for providing RCS-
maintained data for printing in the file list.

