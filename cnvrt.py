import os, sys
import subprocess
import shutil
import random

def getname(idx):
  suf = ''
  if idx < 10:
    suf += '00
  files = os.listdir(infolder)
  random.shuffle(files)
  for f in files:
    shutil.copy(os.path.join(infolder, f), os.path.join(oufolder, getname(glob_idx)))
    glob_idx += 1
