import testharness

def greddychange(coins,amount):
    result = [0] * len(coins)

    for i in xrange(len(coins)-1,-1,-1):
        coinsused = amount//coins[i]
        amount -= coinsused * coins[i]
        result[i] = coinsused

    return result

def greddyItter(coins,amount):
    result = [0] * len(coins)

    for i in xrange(len(coins)-1,-1,-1):

        while coins[i] <= amount:
            amount -= coins[i]
            result[i]+=1

    return result


testharness.runTests(greddychange)