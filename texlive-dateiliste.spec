# revision 16032
# category Package
# catalog-ctan /macros/latex/contrib/dateiliste
# catalog-date 2009-11-04 23:51:05 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-dateiliste
Version:	0.5
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a file list (similar to that offered by
\listfiles), neatly laid out as a table. The main document can
be included in the list, and a command is available for
providing RCS-maintained data for printing in the file list.

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
%{_texmfdistdir}/tex/latex/dateiliste/dateiliste.sty
%doc %{_texmfdistdir}/doc/latex/dateiliste/README
%doc %{_texmfdistdir}/doc/latex/dateiliste/README-de
%doc %{_texmfdistdir}/doc/latex/dateiliste/README-en
%doc %{_texmfdistdir}/doc/latex/dateiliste/README-eo
%doc %{_texmfdistdir}/doc/latex/dateiliste/dateiliste.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dateiliste/dateiliste.dtx
%doc %{_texmfdistdir}/source/latex/dateiliste/dateiliste.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
