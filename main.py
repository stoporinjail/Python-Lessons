import os
import sys
l = input("What lesson did you complete last time? If this is your first time here, click enter and leave this blank..\n[1] I completed lesson 1, but haven't completed lesson 2 yet.\n[2] I completed 2, but haven't completed 3.\n and so on.")
if l == '':
  os.system("python l1.py")
if l == '1':
  os.system("python l2.py")
else:
  print("Only lesson 1 has been released. Please check back on these dates:\n\nLesson 3: ~Febuary 7, 2021\nLesson 4: ~Febuary 7, 2021")