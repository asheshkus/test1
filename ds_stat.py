import os, sys


if __name__ == '__main__':
  d = open("d:/_tst/sstat_da.txt", 'r').readlines()

  strs_c = len(d)

  rc = 0
  rw = 0
  dc = 0
  dw = 0

  sc = 0
  sw = 0

  spaces = 0
  symbols = 0

  space_true = [0, 0]
  symbols_true = [0, 0]

  r_errs_sy = 0
  r_errs_sp = 0

  d_corr_sy = 0
  d_corr_sp = 0

  
  idx = 0
  while idx < strs_c - 4:
    slen = len(d[idx])

    for i in range(0, slen):
      mv = d[idx][i] == ' '
      rv = d[idx + 1][i] == ' '
      dv = d[idx + 2][i] == '0' or d[idx + 2][i] == '1'

      if mv:
        spaces += 1
        if rv:
          space_true[0] += 1
        if dv:
          space_true[1] += 1
      else:
        symbols += 1
        if not rv:
          symbols_true[0] += 1
        if not dv:
          symbols_true[1] += 1

        if d[idx][i] == d[idx + 1][i]:
          sc += 1
        else:
          sw += 1

      if mv and not dv:
        r_errs_sp += 1
        if rv:
          d_corr_sp += 1

      if not mv and dv:
        r_errs_sy += 1
        if not rv:
          d_corr_sy += 1

    idx += 4

  print "spaces: rr", float(space_true[0]) / spaces, "ds", float(space_true[1]) / spaces
  print "symbols: rr", float(symbols_true[0]) / symbols, "ds", float(symbols_true[1]) / symbols
  print "overall: rr", float(symbols_true[0] + space_true[0]) / (symbols + spaces), "ds", float(symbols_true[1] + space_true[1]) / (symbols + spaces)
  print "count: symbols", symbols, "spaces", spaces, "all", symbols + spaces  
  print "character stat:", float(sc) / (sc + sw)  

  print "___"
  print "sym:", r_errs_sy, float(d_corr_sy) / r_errs_sy
  print "spa:", r_errs_sp, float(d_corr_sp) / r_errs_sp
  print "ovr:", r_errs_sy + r_errs_sp, float(d_corr_sy + d_corr_sp) / (r_errs_sy + r_errs_sp)
