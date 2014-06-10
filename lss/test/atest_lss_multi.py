#!/usr/bin/python


import coolfluid as cf
import math


cf.env.log_level = 3 #  1=error, 2=warning, 3=info, 4=debug


list_of_solvers = [
  'GaussianElimination_LongPrecisionComplex',
  'GaussianElimination_LongPrecisionReal',
  'GaussianElimination_ShortPrecisionComplex',
  'GaussianElimination_ShortPrecisionReal',
  'LAPACK_LongPrecisionComplex',
  'LAPACK_LongPrecisionReal',
  'LAPACK_ShortPrecisionComplex',
  'LAPACK_ShortPrecisionReal',
  'GMRES',
  'wsmp.wsmp',
  'mkl.dss',
  'mkl.iss_fgmres',
  'mkl.pardiso',
# 'pardiso.pardiso',  # incompatible with any of the mkl solvers (in the same run)
  ]
for solver in list_of_solvers:
  lss = cf.root.create_component('MySolver_' + solver,'cf3.lss.' + solver)


  print
  print solver
  lss.initialize(i=4,j=4,k=2)
  lss.A = [  1,  0,  0,  0,
             0, -1,  0,  0,
             0,  0,  2,  0,
             0,  0,  0,  3 ]
  lss.b = [1000]
  lss.x = [  2,  4,
             4,  8,
             6, 12,
             8, 16 ]
  #lss.output(A=3,b=3,x=3)
  lss.multi(alpha=0.001,beta=1.e-3)
  lss.output(A=1,b=1,x=3)

