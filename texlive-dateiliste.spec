# revision 27974
# category Package
# catalog-ctan /macros/latex/contrib/dateiliste
# catalog-date 2012-10-15 00:17:21 +0200
# catalog-license lppl
# catalog-version 0.6
Name:		texlive-dateiliste
Version:	0.6
Release:	3
Summary:	Extensions of the \listfiles concept
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dateiliste
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dateiliste.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dateiliste.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dateiliste.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a file list (similar to that offered by
\listfiles), neatly laid out as a table. The main document can
be included in the list, and a command is available for
providing RCS-maintained data for printing in the file list.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dateiliste/dateiliste.sty
%doc %{_texmfdistdir}/doc/latex/dateiliste/README
%doc %{_texmfdistdir}/doc/latex/dateiliste/README-de
%doc %{_texmfdistdir}/doc/latex/dateiliste/README-en
%doc %{_texmfdistdir}/doc/latex/dateiliste/README-eo
%doc %{_texmfdistdir}/doc/latex/dateiliste/dateiliste.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dateiliste/dateiliste.dtx
%doc %{_texmfdistdir}/source/latex/dateiliste/dateiliste.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
