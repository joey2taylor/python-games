#!/usr/bin/python
from time import sleep
a = 5
b = 0

def meth(c):
  print("GIRAFFE")
  sleep(c)
  print("DUCK")
  sleep(c)

while b<a:
  meth(2)
  b = b + 1
print(";D")
