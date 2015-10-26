def changedp(coins,amount):
    result = [0] * len(coins)

    minCoins = [0] + [float('inf')] * amount
    trace = [0] * (amount + 1)

    for tableIndex in xrange(1,amount+1):
        coinIndex = 0
        while coinIndex < len(coins) and coins[coinIndex] <= tableIndex:
            if minCoins[tableIndex-coins[coinIndex]] + 1 < minCoins[tableIndex]:
                minCoins[tableIndex] = minCoins[tableIndex-coins[coinIndex]]+1
                trace[tableIndex]=coinIndex
            coinIndex+=1


    traceIndex = amount
    while traceIndex > 0:
        coinused = trace[traceIndex]
        result[coinused] +=1
        traceIndex -= coins[coinused]

    return result

if __name__ == '__main__':
    import testharness
    testharness.runTests(changedp)