# It is too easy to mpiexec an application that also uses OpenMP multi-threading.
# This is a recipe for disaster, so let's practically disable OpenMP unless the
# mpi run script raises this limit.
export OMP_NUM_THREADS=1

