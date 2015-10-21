import testharness

def changeslow(coins,amount):
    result = [0] * len(coins)

    #if amount > 5: print amount

    #base case
    for i in range(len(coins)):
        if coins[i] == amount:
            result[i] = 1
            return result

    bestmin = float('inf')
    
    #recursive case
    for i in range(1,amount):
        candidateA = changeslow(coins,i)
        candidateB = changeslow(coins,amount-i)

        if sum(candidateA)+sum(candidateB) < bestmin:
            bestmin = sum(candidateA)+sum(candidateB)
            result = [candidateA[i] + candidateB[i] for i in xrange(len(coins))]

    return result

testharness.runTests(changeslow)