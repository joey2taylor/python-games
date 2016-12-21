#!/usr/bin/python
import sys

def meth(hi1, hi2, hi3):
    if hi1 == "1":
        print hi2
    if hi1 == 1:
        print hi3
    if hi1 == 2:
        print hi2
        print hi3
by1 = int(sys.argv[1])
by2 = sys.argv[2]
by3 = sys.argv[3]
while True:
    meth(by1, by2, by3)
