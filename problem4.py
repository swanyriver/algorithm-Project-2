import time, timeit
from changedp import changedp
from changegreedy import changegreedy

values = [1, 5, 10, 25, 50]

print "amount, greedy coins, greedy time, dp coins, dp time"

for amount in range(2010,2201,5):
  print amount,",",
  print sum(changegreedy(values,amount)),",",
  print timeit.timeit(stmt='changegreedy.changegreedy(%s,%s)'%(str(values),str(amount)),setup="import changegreedy",timer=time.clock,number=1000),",",
  print sum(changedp(values,amount)),",",
  print timeit.timeit(stmt='changedp.changedp(%s,%s)'%(str(values),str(amount)),setup="import changedp",timer=time.clock,number=100)*10