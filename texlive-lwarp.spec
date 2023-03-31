Name:		texlive-lwarp
Version:	63905
Release:	2
Summary:	Converts LaTeX to HTML
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lwarp
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lwarp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lwarp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lwarp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package converts LaTeX to HTML by using LaTeX to process
the user's document and generate HTML tags. External utility
programs are only used for the final conversion of text and
images. Math may be represented by SVG files or MathJax.
Hundreds of LaTeX packages are supported, and their load order
is automatically verified. Documents may be produced by LaTeX,
LuaLaTeX, XeLaTeX, and by several CJK engines, classes, and
packages. A texlua script automates compilation, index,
glossary, and batch image processing, and also supports
latexmk. Configuration is semi-automatic at the first manual
compile. Support files are self-generated. Print and HTML
versions of each document may coexist. Assistance is provided
for HTML import into EPUB conversion software and word
processors. Requirements include the commonly-available Poppler
utilities, and Perl. Detailed installation instructions are
included for each of the major operating systems and TeX
distributions. A quick-start tutorial is provided.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/latex/lwarp
%{_texmfdistdir}/texmf-dist/tex/latex/lwarp
%{_texmfdistdir}/texmf-dist/scripts/lwarp
%doc %{_texmfdistdir}/texmf-dist/doc/latex/lwarp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
