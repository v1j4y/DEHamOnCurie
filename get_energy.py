#!/usr/bin/env python

import re
import sys
import os
from shutil import copyfile

from tjtemp import tJ_file

J = 0.0
for i in range(16):
  J += (i)*(0.2/16) + 0.01
  path = os.getcwd() + "/J_" + str(i)
  dst = path + "/tJ_4x4.out"
  done = False
# print dst
  with open(dst,"r") as f:
    getE = False
    totE = 0
    for lines in f.readlines():
      if getE and totE < 2:
        if totE == 0:
          E1 = lines.split()[0]
        else:
          E2 = lines.split()[0]
        totE += 1
      if "----------------- ----------------- ------------------" in lines:
        getE = True
  print J,"\t\t", E1,"\t\t", E2
