import os, sys
import subprocess
import shutil
import random

def getname(idx):
  suf = ''
  if idx < 10:
    suf += '00'
  elif idx < 100:
    suf += '0'
  suf += str(idx)
  return 'img_' + suf + '.jpg'

if __name__ == '__main__':
  infolder = 'D:/_ocr11/logo_negative/images_selected'
  oufolder = 'D:/_ocr11/logo_negative/logo_neg'
  glob_idx = 0
  files = os.listdir(infolder)
  random.shuffle(files)
  for f in files:
    shutil.copy(os.path.join(infolder, f), os.path.join(oufolder, getname(glob_idx)))
    glob_idx += 1
