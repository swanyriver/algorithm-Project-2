import time, timeit


def avg(l): return sum(l)/len(l)

avg(timeit.Timer(stmt='changedp.changedp([1,5,10,25],186)',setup="import changedp",timer=time.clock).repeat(10,1))
