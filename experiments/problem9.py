from changegreedy import changegreedy
from changedp import changedp

TOP = 1000

for b in range(2,11):
  x = 1
  values = [x]
  while x<TOP:
    x*=b
    values.append(x)

  print values
  #raw_input()

  incorrect = 0

  for a in range(1,TOP):
    g = sum(changegreedy(values,a))
    d = sum(changedp(values,a))

    #print "amount:%d  DP:%d  Greedy:%d"%(a,d,g)
    if g>d: incorrect +=1

  print "for base:%d there were %d non optimal Greedy outputs"%(b,incorrect)



