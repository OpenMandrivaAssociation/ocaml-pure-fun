Name:		ocaml-pure-fun
Version:	1.0.8
Release:        %mkrel 4
Summary:        Okasaki's Purely Functional Datastructures in OCaml
License:        free-software
##license notice writen in the files:
#
#  Unless this violates copyrights of the original sources, the following
#  licence applies to this file:
#
#  This source code is free software; you can redistribute it and/or
#  modify it without any restrictions. It is distributed in the hope
#  that it will be useful, but WITHOUT ANY WARRANTY.
Group:          Development/Other
URL:		http://www.ocaml.info/home/ocaml_sources.html#pure-fun
Source0:	http://hg.ocaml.info/release/pure-fun/archive/pure-fun-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/pure-fun/archive/release-%{version}.tar.bz2 > pure-fun-release-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
These files contain an SML-to-OCAML translation of source examples taken
from the following book:

    Purely Functional Data Structures
    Chris Okasaki
    Cambridge University Press, 1998
    Copyright (C) 1998 Cambridge University Press

%package        doc
Summary:        Development files for %{name}
Group:          Development/Other

%description    doc
These files contain an SML-to-OCAML translation of source examples taken
from the following book:

    Purely Functional Data Structures
    Chris Okasaki
    Cambridge University Press, 1998
    Copyright (C) 1998 Cambridge University Press

%prep
%setup -q -n pure-fun-release-%{version}

%build

%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}

%files doc
%defattr(-,root,root)
%doc README.txt README.okasaki Changes
%doc chp*.ml

