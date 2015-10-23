import time, timeit


def avg(l): return sum(l)/len(l)

#avg(timeit.Timer(stmt='changedp.changedp([1,5,10,25],186)',setup="import changedp",timer=time.clock).repeat(10,1))

TestCases=["[1,2,4,8],15","[1,3,7,12],29","[1,3,7,12],31"]
for tc in TestCases:
  print timeit.timeit(stmt='changeslow.changeslow(%s)'%tc,setup="import changeslow",timer=time.clock,number=1)

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