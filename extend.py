# on my machine, i ran this with:  
#   python3.13 -B extend.py ../moot/optimize/[comp]*/*.csv
import stats
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
  
  def guess(N,d):
    some = random.choices(d.rows,k=N)
    some = d.clone().adds(some).chebyshevs().rows
    return some
  
  somes = []
  if x<6:
    for N in [20,30,40,50]:
      dumb = [guess(N,d) for _ in range(20)]
      dumb = [d.chebyshev(lst[0]) for lst in dumb]
      somes.append(stats.SOME(dumb,txt=f"dumb, {N}"))
      the.Last = N
      smart = [d.shuffle().activeLearning() for _ in range(20)]
      smart = [d.chebyshev(lst[0]) for lst in smart]
      somes.append(stats.SOME(smart,txt=f"smart, {N}"))
    show([train])
    stats.report(somes)
    
  
  
  return [dim, size, x,len(d.cols.y), len(d.rows),numeric, symbols ,train[17:]]

random.seed(the.seed) #  not needed here, but good practice to always take care of seeds
show(["dim", "size","xcols","ycols","rows","numcols","symcols","file"])
show(["------"] * 9)
[myfun(arg) for arg in sys.argv if arg[-4:] == ".csv"]
