#!/bin/bash 
#SBATCH -J DEHam
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks-per-core=1
#SBATCH --mem=9000
#####################################################
module purge
module load gcc/9.2.0 python/python-3.7.0-gcc-8.2.0 intel/2019.3 arpack-ng/3.7.0-gcc-9.2.0 petsc/3.12.3-gcc-9.2.0 slepc/3.12.0-gcc-9.2.0 openmpi/3.1.5-gcc-9.2.0-slurm irpf90/1.7.7-gcc-9.2.0


GMS=ex1


###################################################
fich=tJ_heis4
 
INPUT=$fich.inp
OUTPUT=$fich.out 
ICI=$PWD 
#####################################################




##########################################################
##########################################################
mpirun -n 1 ./$GMS $INPUT  > $ICI/$OUTPUT



