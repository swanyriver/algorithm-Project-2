There is a testharness.py file that the other 3 programs import for handling the file reading.
The three programs launch as specified:
python algorithm.py [input filename]

be cautious with the tab key, the instructions appeared to request that the .txt suffix be left of the execution command.
so if coin.txt exist in the directory run the three programs as such:

python changegreedy.py coin
python changedp.py coin
python changeslow.py coin


Change Slow:
This program is expectedly slow, slower even for being implemented in Python
Expect it to never finish for values greater than 35
the running time was found to be
A=15 few milliseconds
A=29 a few minutes
A=31 ~10 minutes
A=40 >20 hours


the "experiments" directory contains scripts used to test for correctness and record coin amounts and run times 
