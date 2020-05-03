from os import system
import os
import sys
import time
info = input("Paste info here!:   ")
text = info
file = open('info.txt', 'w')
file.write(text)
file.close()
print("leaking info to database!")

system('git add .')
system('git commit -m "info"')
system('git push -f origin master')
print("Info Is now public!")

