from sys import argv,exit
import sys
import string

#check for provided input file
if len(argv) < 2:
    print "please provide a test cases file"
    exit(1)

#open file for reading
testcasesF = open(argv[1] + '.txt','r')

#check that file opened successfully
if not testcasesF:
    print "file not found"
    exit(1)

#redirect standard output to file
#sys.stdout = open(argv[1] + 'change.txt', 'w')


BADCHARS = string.maketrans('','').translate(None,'0123456789,')

def fileTests():
    while(1):
        coins = testcasesF.readline()
        amount = testcasesF.readline()

        if coins and amount:

            coins = [int(num) for num in coins.translate(None,BADCHARS).split(',')]
            coins.sort()
            amount = int(amount.translate(None,BADCHARS+','))

            yield coins,amount

        else: break


def runTests(func):
    for coins,amount in fileTests():
        used = func(coins,amount)
        
        #requested output
        print used
        print sum(used)

        #testing for correctness output
        # print coins, amount
        # print used
        # eq = [used[i] * coins[i] for i in range(len(coins))]
        # print eq, '=', sum(eq)
        # print "coins used:  ", sum(used)
        # print '-------------------------------------------------'