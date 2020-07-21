#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tmvnsim
Version  : 1.0.2
Release  : 1
URL      : https://cran.r-project.org/src/contrib/tmvnsim_1.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tmvnsim_1.0-2.tar.gz
Summary  : Truncated Multivariate Normal Simulation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-tmvnsim-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
Unlike Gibbs sampling which can get stuck in one truncation sub-region depending on initial values, this package allows 
  truncation based on disjoint regions that are created by truncation of absolute values. The GHK algorithm uses simple Cholesky
  transformation followed by recursive simulation of univariate truncated normals hence there are also no convergence issues. 
  Importance sample is returned along with sampling weights, based on which, one can calculate integrals over truncated regions
  for multivariate normals.

%package lib
Summary: lib components for the R-tmvnsim package.
Group: Libraries

%description lib
lib components for the R-tmvnsim package.


%prep
%setup -q -c -n tmvnsim
cd %{_builddir}/tmvnsim

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595346284

%install
export SOURCE_DATE_EPOCH=1595346284
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tmvnsim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tmvnsim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tmvnsim
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tmvnsim || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tmvnsim/DESCRIPTION
/usr/lib64/R/library/tmvnsim/INDEX
/usr/lib64/R/library/tmvnsim/Meta/Rd.rds
/usr/lib64/R/library/tmvnsim/Meta/features.rds
/usr/lib64/R/library/tmvnsim/Meta/hsearch.rds
/usr/lib64/R/library/tmvnsim/Meta/links.rds
/usr/lib64/R/library/tmvnsim/Meta/nsInfo.rds
/usr/lib64/R/library/tmvnsim/Meta/package.rds
/usr/lib64/R/library/tmvnsim/NAMESPACE
/usr/lib64/R/library/tmvnsim/R/tmvnsim
/usr/lib64/R/library/tmvnsim/R/tmvnsim.rdb
/usr/lib64/R/library/tmvnsim/R/tmvnsim.rdx
/usr/lib64/R/library/tmvnsim/help/AnIndex
/usr/lib64/R/library/tmvnsim/help/aliases.rds
/usr/lib64/R/library/tmvnsim/help/paths.rds
/usr/lib64/R/library/tmvnsim/help/tmvnsim.rdb
/usr/lib64/R/library/tmvnsim/help/tmvnsim.rdx
/usr/lib64/R/library/tmvnsim/html/00Index.html
/usr/lib64/R/library/tmvnsim/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tmvnsim/libs/tmvnsim.so