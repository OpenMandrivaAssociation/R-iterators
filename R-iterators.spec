%bcond_with       bootstrap
%global packname  iterators
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.5
Release:          2
Summary:          Iterator construct for R
Group:            Sciences/Mathematics
License:          Apache License (== 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-utils 
%if %{without bootstrap}
Requires:         R-foreach R-RUnit 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-utils
%if %{without bootstrap}
BuildRequires:    R-foreach R-RUnit 
%endif

%description
Support for iterators, which allow a programmer to traverse through all
the elements of a vector, list, or other collection of data.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests
