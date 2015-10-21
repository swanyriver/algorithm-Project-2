import testharness

def dummy(coins,amount):
    return [x//2 for x in coins]

testharness.runTests(dummy)