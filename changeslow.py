def changeslow(coins,amount):
    result = [0] * len(coins)

    #base case
    for i in range(len(coins)):
        if coins[i] == amount:
            result[i] = 1
            return result

    bestmin = float('inf')
    
    #recursive case
    # for i in range(1,amount):
    #     candidateA = changeslow(coins,i)
    #     candidateB = changeslow(coins,amount-i)

    #     if sum(candidateA)+sum(candidateB) < bestmin:
    #         bestmin = sum(candidateA)+sum(candidateB)
    #         result = [candidateA[i] + candidateB[i] for i in xrange(len(coins))]

    # return result

    return min( ( map(add,changeslow(coins,i),changeslow(coins,amount-i)) for i in range(1,amount) ) , key=sum )


if __name__ == '__main__':
    import testharness
    from operator import add
    testharness.runTests(changeslow)