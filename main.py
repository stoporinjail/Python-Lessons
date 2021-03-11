import os
import sys
l = input("How many lessons have you completed? Leave blank or put 0 if you are new.")
if l == '0' or l == '':
  os.system("python l1.py")
  sys.exit("Have a great day! Run this again to start the next lesson.")
if l == '1':
  os.system("python l2.py")
  sys.exit("Have a great day! Run this again to start the next lesson.")
if l == '2':
  os.system("python l3.py")
  sys.exit("Have a great day! Run this again to start the next lesson.")
if l == '3':
  os.system("python l4_QUIZ.py")
  sys.exit("Have a great day! Run the program again to start the next lesson.")
else:
  print("Only lesson 1, 2, and 3, and 4 have been released.")