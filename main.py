import os
import sys
l = input("What lesson did you complete last time? If this is your first time here, click enter and leave this blank..\n[1] I completed lesson 1, but haven't completed lesson 2 yet.\n[2] I completed 2, but haven't completed 3.\n and so on.")
if l == '':
  os.system("python l1.py")
  sys.exit("Run this again to continue to the next lesson!")
else:
  print("Only lesson 1 has been released. Please check back on these dates:\n\nLesson 2: ~Febuary 6, 2021\nLesson 3: ~Febuary 8, 2021")