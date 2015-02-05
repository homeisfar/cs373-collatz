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
# ------------
# collatz_eval
# ------------

def collatz_eval () :
    """
    Find the cycle length of i.
    """

    c = 1
    i = 1
    v = 1
    while i < 31 :
        c = 1
        v = i
        while v > 1 :
            if (v % 2) == 0 :
                v = (v // 2)
            else :
                v = v + (v >> 1) + 1
                c+=1 
            c+=1
        sys.stdout.write(str(c) +", ")
        i = i + 1
    return c


# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    #i, j = collatz_read(s)
    v    = collatz_eval()
    #collatz_print(w, i, v)




if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)
