import sys
import os
Q1 = os.environ.get('Q1_ANSWER')
Q2 = os.environ.get('Q2_ANSWER')
Q3 = os.environ.get('Q3_ANSWER')

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
correct = 0
wrong = 0
w("Hello, I am stoporinjail, your instructor.")
w("Today, we will not really have a lesson, but we will be doing a test on earlier lessons.")
w("If you do not answer, it will mark the question as wrong.")
w("Let's get started!")
noinput("What is the format for a variable? \n[1]. var = variable name;\n'text'\n[2]. variablename = \n'text'\n[3] variablename = 'text'\n [4] variable name = \n'value'")
q1 = input(' ')
if q1 == Q1:
  correct += 1
else:
  wrong += 1
noinput("What is an f string?\n[1] It allows you to print a variable using f before ' and { before the variable\n[2] It prints a bunch of f's out.\n[3] It is a variable that is always there\n [4] All of the above")
q2 = input(' ')
if q2 == Q2:
  correct += 1
else:
  wrong += 1
noinput("What does sys.exit() do?\n[1] Finds out your system details\n [2] Exits you from the code program.\n[3] Exits the browser or app you are doing this.\n[4] Your computer shuts down.")
q3 = input(' ')
if q3 == Q3:
  correct += 1
else:
  wrong += 1
w("That is all for today!")
w("Questions? Concerns? Drop a comment at https://repl.it/@stoporijail/Python-Lessons")