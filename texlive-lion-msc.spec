Name:		texlive-lion-msc
Version:	55415
Release:	2
Summary:	LaTeX class for B.Sc. and M.Sc. reports at Leiden Institute of Physics (LION)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lion-msc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lion-msc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lion-msc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX class for B.Sc. and M.Sc. reports at Leiden Institute of
Physics (LION). The purpose of this class is twofold: It
creates a uniform layout of the student theses from our
department. More importantly it contains several fields on the
front-page that the user needs to fill that are used in the
university administration (name, student number and name of
supervisor). Students are free to change the layout of the text
but should leave the title page as it is.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/lion-msc
%{_texmfdistdir}/bibtex/bst/lion-msc
%doc %{_texmfdistdir}/doc/latex/lion-msc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
