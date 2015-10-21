from sys import argv,stdout,exit
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
sys.stdout = open(argv[1] + 'change.txt', 'w')


BADCHARS = string.maketrans('','').translate(None,'0123456789,')

def fileTests():
    while(1):
        coins = testcasesF.readline()
        amount = testcasesF.readline()

    if coins and amount:

        coins = [int(num) for num in coins.translate(None,BADCHARS).split(',')
        amount = int(amount.translate(None,BADCHARS+','))

        yield coins,amount

    else break


def runTests(func):
    