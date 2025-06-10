# Disable the Intel warning about deprecated C++ classic compilers (10441)
# Disable the Intel warning about deprecated Fortran compilers (10448)
# Disable the overriding '-qopenmp-stubs' with '-qopenmp' issue (10121)
export __INTEL_PRE_CFLAGS="-diag-disable=10441,10448,10121"

