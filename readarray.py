from sys import argv,stdout,exit
import string

if len(argv) < 2:
    print "please provide a test cases file"
    exit(1)

testcasesF = open(argv[1] + '.txt','r')

if not testcasesF:
    print "file not found"
    exit(1)

sys.stdout = open(argv[1] + 'change.txt', 'w')


BADCHARS = string.maketrans('','').translate(None,'0123456789,')

