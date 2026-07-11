%global tl_name lwarp
%global tl_revision 79391

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.922
Release:	%{tl_revision}.1
Summary:	Converts LaTeX to HTML
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lwarp
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lwarp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lwarp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lwarp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(lwarp.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package converts LaTeX to HTML by using LaTeX to process the user's
document and generate HTML tags. External utility programs are only used
for the final conversion of text and images. Math may be represented by
SVG files or MathJax. Hundreds of LaTeX packages are supported, and
their load order is automatically verified. Documents may be produced by
LaTeX, LuaLaTeX, XeLaTeX, and by several CJK engines, classes, and
packages. A texlua script automates compilation, index, glossary, and
batch image processing, and also supports latexmk. Configuration is
semi-automatic at the first manual compile. Support files are self-
generated. Print and HTML versions of each document may coexist.
Assistance is provided for HTML import into EPUB conversion software and
word processors. Requirements include the commonly-available Poppler
utilities, and Perl. Detailed installation instructions are included for
each of the major operating systems and TeX distributions. A quick-start
tutorial is provided.

