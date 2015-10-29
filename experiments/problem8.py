import time, timeit,random


values = [1]
while len(values)<200:
  values.append(values[-1]+int(random.random()*10)+1)


amount = 10000

print "amount, greedy time, dp time"

for i in range(5,200,5):

  print i,",",
  print timeit.timeit(stmt='changegreedy.changegreedy(%s,%s)'%(str(values[:i]),str(amount)),setup="import changegreedy",timer=time.clock,number=1000),",",
  print timeit.timeit(stmt='changedp.changedp(%s,%s)'%(str(values[:i]),str(amount)),setup="import changedp",timer=time.clock,number=10)*100
