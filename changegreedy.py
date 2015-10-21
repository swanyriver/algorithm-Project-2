import testharness

def greddychange(coins,amount):
    result = [0] * len(coins)

    for i in range(len(coins)-1,-1,-1):
        coinsused = amount//coins[i]
        amount -= coinsused * coins[i]
        result[i] = coinsused

    return result


testharness.runTests(greddychange)