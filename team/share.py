#by Felix
import random
import os
import time

rows, columns = os.popen('stty size', 'r').read().split()

chars_to_print = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
colors = ["\033[01;32m","\033[00;32m", "\033[00;30m", "\033[00;30m", "\033[00;30m", "\033[00;30m", "\033[00;30m", "\033[00;30m", "\033[00;30m", "\033[00;30m", "\033[00;30m", "\033[00;30m"]


line_width = int(columns)

while True:
	for i in range(line_width):
		print(random.choice(colors), random.choice(chars_to_print),sep='',end='')
	print()
	time.sleep(0.04)
#End by Felix

a = 1
b= 69

if a == b:
  c = 2
else:
  c = 69420

print(c)
print("never gonna give you up never gonna let you down")
print("Hello")
print("hello")
print("Hello There")