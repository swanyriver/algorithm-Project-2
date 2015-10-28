import time, timeit
from changeslow import changeslow
from changedp import changedp
from changegreedy import changegreedy


def avg(l): return sum(l)/len(l)

#avg(timeit.Timer(stmt='changedp.changedp([1,5,10,25],186)',setup="import changedp",timer=time.clock).repeat(10,1))

def cointime(values,amount):
  intime = time.clock()
  coins = changeslow(values,amount)
  outime = time.clock() - intime
  return sum(coins),outime*1000

def cointimedp(values,amount):
  outtime = timeit.timeit(stmt='changedp.changedp(%s,%s)'%(str(values),str(amount)),setup="import changedp",timer=time.clock,number=100)*10
  coins = changedp(values,amount)
  return sum(coins),outtime

def cointimegreedy(values,amount):
  outtime = timeit.timeit(stmt='changegreedy.changegreedy(%s,%s)'%(str(values),str(amount)),setup="import changegreedy",timer=time.clock,number=1000)
  coins = changedp(values,amount)
  return sum(coins),outtime




valueset = [
[1,5,10,25,50],
[1,2,6,12,24,48,60],
[1, 6, 13, 37, 150],
[1] + range(2,31,2), 
]


#print "amount,",
#for v in valueset[:-1]: print "\"%s:Coins\",\"%s:Time\","%(str(v),str(v)),
#print "\"%s:Coins\",\"%s:Time\""%(str(valueset[-1]),str(valueset[-1]))

# for amount in range(10,31) + [35]:
#   print amount,",",
#   for v in valueset[:-1]: print "%d,%f,"%cointime(v,amount),
#   print "%d,%f"%cointime(valueset[-1],amount)

print "amount, slowtime, greedytime, dptime"

for amount in range(10,31) + [35]:
  print amount,",",
  print cointime([1],amount)[1],
  print cointimegreedy([1],amount)[1],
  print cointimedp([1],amount)[1]



# TestCases=[("[1,2,4,8],15", [1,2,4,8],15),("[1,3,7,12],29",[1,3,7,12],29),("[1,3,7,12],31",[1,3,7,12],31)]
# for tc,values,amount in TestCases:
#   print timeit.timeit(stmt='changeslow.changeslow(%s)'%tc,setup="import changeslow",timer=time.clock,number=1),

#   intime = time.clock()
#   changeslow(values,amount)
#   outime = time.clock() - intime

#   print " vs %f  measured manually"%outime



#PROBLEM 4
# coins = "[1,5,10,25,50],"
# TestCases = [ coins + str(x) for x in xrange(2010,2201,5)]
# print TestCases


#measuring millisecond
# print "Dynamic solution"
# for tc in TestCases:
#   print timeit.timeit(stmt='changedp.changedp(%s)'%tc,setup="import changedp",timer=time.clock,number=100)*10

# print "------------------------"
# print "Greedy solution"
# for tc in TestCases:
#   print timeit.timeit(stmt='changegreedy.changegreedy(%s)'%tc,setup="import changegreedy",timer=time.clock,number=1000)