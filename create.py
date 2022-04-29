#!/usr/bin/env python

import re
import sys
import os
from shutil import copyfile

from tjtemp import tJ_file

J = 0.0
for i in range(16):
  J += (i)*(0.2/16) + 0.01
  filenew = re.sub("0.1430",str(J),tJ_file)
  print(J)
  path = os.getcwd() + "/J_" + str(i)
  dst = path + "/tJ_heis4.inp"
  print(dst)
  os.mkdir(path)
  copyfile("./tJ_heis4.inp",dst)
  text_file = open(dst, "w")
  text_file.write(filenew)
  text_file.close()
  print("Done"+str(i))
