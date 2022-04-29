#!/usr/bin/env python

import re
import sys
import os
from shutil import copyfile, copymode

from tjtemp import tJ_file

J = 0.0
for i in range(16):
  J += (i)*(0.2/16) + 0.01
  filenew = re.sub("0.1430",str(J),tJ_file)
  print(J)
  path = os.getcwd() + "/J_" + str(i)
  srs = os.getcwd() + "/job.sh"
  dst = path + "/job.sh"
  print(srs)
  print(dst)
  copyfile(srs,dst)
  srs = os.getcwd() + "/ex1"
  st = os.stat(srs)
  dst = path + "/ex1"
  copyfile(srs,dst)
  copymode(srs,dst)
  #os.chown(dst,st.st_uid,st.st_gid)
# os.mkdir(path)
