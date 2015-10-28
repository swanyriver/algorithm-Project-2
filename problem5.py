import time, timeit
from changedp import changedp
from changegreedy import changegreedy

vA = [1,2,6,12,24,48,60]
vB = [1, 6, 13, 37, 150]

#print "amount, greedy coins v1, greedy time v1, dp coins v1, dp time v1, greedy coins v2, greedy time v2, dp coins v2, dp time v2, "

# for amount in range(2000,2201):
#   print amount,",",
#   print sum(changegreedy(vA,amount)),",",
#   print timeit.timeit(stmt='changegreedy.changegreedy(%s,%s)'%(str(vA),str(amount)),setup="import changegreedy",timer=time.clock,number=1000),",",
#   print sum(changedp(vA,amount)),",",
#   print timeit.timeit(stmt='changedp.changedp(%s,%s)'%(str(vA),str(amount)),setup="import changedp",timer=time.clock,number=100)*10,",",

#   print sum(changegreedy(vB,amount)),",",
#   print timeit.timeit(stmt='changegreedy.changegreedy(%s,%s)'%(str(vB),str(amount)),setup="import changegreedy",timer=time.clock,number=1000),",",
#   print sum(changedp(vB,amount)),",",
#   print timeit.timeit(stmt='changedp.changedp(%s,%s)'%(str(vB),str(amount)),setup="import changedp",timer=time.clock,number=100)*10

# wronga = 0
# wrongb = 0
# n = len(range(2000,2201))

# for amount in range(2000,2201):
#   if sum(changegreedy(vA,amount)) > sum(changedp(vA,amount)): wronga +=1
#   if sum(changegreedy(vB,amount)) > sum(changedp(vB,amount)): wrongb +=1

# print "v1 greedy wrong: %d out of: %d for an average of:%f incorecct"%(wronga,n,float(wronga)/float(n))
# print "v2 greedy wrong: %d out of: %d for an average of:%f incorecct"%(wrongb,n,float(wrongb)/float(n))


for amount in range(2000,2201):
  if sum(changegreedy(vA,amount)) > sum(changedp(vA,amount)): print "wrong",
  else: print "-----",
  if sum(changegreedy(vB,amount)) > sum(changedp(vB,amount)): print "wrong"
  else: print "-----"
