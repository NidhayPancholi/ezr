# on my machine, i ran this with:  
#   python3.13 -B extend.py ../moot/optimize/[comp]*/*.csv

import sys,random
import ezr
from ezr import the, DATA, csv, dot

def show(lst):
  return print(*[f"{word:6}" for word in lst], sep="\t")

def myfun(train):
  d    = DATA().adds(csv(train))
  x    = len(d.cols.x)
  size = len(d.rows)
  numeric = 0
  symbols = 0
  for col in d.cols.x:
    if isinstance(col,ezr.NUM):
      numeric +=1
    else:
      symbols+=1
  
  dim  = "small" if x <= 5 else ("med" if x < 12 else "hi")
  size = "small" if size< 500 else ("med" if size<5000 else "hi")
  return [dim, size, x,len(d.cols.y), len(d.rows),numeric, symbols ,train[17:]]

random.seed(the.seed) #  not needed here, but good practice to always take care of seeds
show(["dim", "size","xcols","ycols","rows","numcols","symcols","file"])
show(["------"] * 9)
[show(myfun(arg)) for arg in sys.argv if arg[-4:] == ".csv"]
