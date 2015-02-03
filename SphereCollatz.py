#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

# from Collatz import collatz_solve

# ----
# main
# ----




"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the directory Collatz.html
"""

#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# With student edits by Ali Homafar
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j > 0
    assert i < 1000000
    assert j < 1000000
    
    if i > j :
    	temp = i
    	i = j
    	j = temp
    if j // 2 > i :
    	i = j // 2
    c = 1
    retval = c
    while i < j :
    	v = i
    	c = 1
    	while v > 1:
    		if (v % 2) == 0 :
    			v = (v // 2)
    		else :
    			v = (v * 3) + 1
    		c+=1
    		if c > retval :
    			retval = c
    	i = i + 1
    return retval

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)




if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)