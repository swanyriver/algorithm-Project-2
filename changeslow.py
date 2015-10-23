def best(tupleoflists):
    return len(tupleoflists[0]) + len(tupleoflists[1])

def slowhelper(coins,amount):
    if amount in coins: return [amount]

    bestki = min( ( (slowhelper(coins,i),slowhelper(coins,amount-i)) for i in range(1,amount//2+1) ), key = best )

    bestki[0].extend(bestki[1])

    return bestki[0]


def changeslow(coins,amount):
    result = [0] * len(coins)

    coinsused = slowhelper(coins,amount)
    indexes = {}
    for i in range(len(coins)): indexes[coins[i]]=i

    for c in coinsused: result[indexes[c]]+=1

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