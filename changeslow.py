## in order to get more recordable times this algorithm has been 
## optimized for python by using inplied loops wherever possible
## also instead of returning an array of coin totals during recursion
## the recursive function returns a list of coins used that are then tallied
## by the original function
##
## it is still of course very slow
def best(tupleoflists):
    return len(tupleoflists[0]) + len(tupleoflists[1])

def slowhelper(coins,amount):
    if amount in coins: return [coins.index(amount)]

    bestki = min( ( (slowhelper(coins,i),slowhelper(coins,amount-i)) for i in range(1,amount//2+1) ), key = best )

    bestki[0].extend(bestki[1])

    return bestki[0]


def changeslow(coins,amount):
    result = [0] * len(coins)

    coinsUsed = slowhelper(coins,amount)

    #turn returned array of coin values used into 
    for i in coinsUsed:
        result[i]+=1

    return result

if __name__ == '__main__':
    import testharness
    testharness.runTests(changeslow)




#################################################
#####   too slow version   ######################
#################################################
# from operator import add
# def changeslow(coins,amount):
#     result = [0] * len(coins)

#     #base case
#     for i in range(len(coins)):
#         if coins[i] == amount:
#             #print "returned coin: " + str(coins[i])
#             result[i] = 1
#             return result

#     bestmin = float('inf')
    
#     #recursive case
#     # for i in range(1,amount):
#     #     candidateA = changeslow(coins,i)
#     #     candidateB = changeslow(coins,amount-i)

#     #     if sum(candidateA)+sum(candidateB) < bestmin:
#     #         bestmin = sum(candidateA)+sum(candidateB)
#     #         result = [candidateA[i] + candidateB[i] for i in xrange(len(coins))]

#     # return result

#     return min( ( map(add,changeslow(coins,i),changeslow(coins,amount-i)) for i in range(1,amount//2+1) ) , key=sum )