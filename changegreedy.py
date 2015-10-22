def greddychange(coins,amount):
    result = [0] * len(coins)

    for i in xrange(len(coins)-1,-1,-1):
        # #coins[i] used = amount/coins[i]
        # amount = remainder, or amount - (amount//coins[i]) * coins[i]
        result[i],amount = divmod(amount,coins[i])

    return result

def greddyItter(coins,amount):
    result = [0] * len(coins)

    for i in xrange(len(coins)-1,-1,-1):

        while coins[i] <= amount:
            amount -= coins[i]
            result[i]+=1

    return result

if __name__ == '__main__':
    import testharness
    testharness.runTests(greddychange)