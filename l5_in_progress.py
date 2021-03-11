import sys
sys.exit(0)
from sys import stdout as s
from time import sleep as j
def w(print):
  for i in print:
    j(.03)
    s.write(i)
    s.flush()
  next = input()
def noinput(print):
  for i in print:
    j(.03)
    s.write(i)
    s.flush()