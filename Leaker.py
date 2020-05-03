from os import system
import os
import sys
import time


BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan    = "\033[96m"
END = '\033[0m'

if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(BLUE + """  
    ██╗███╗   ██╗███████╗ ██████╗     ██╗     ███████╗ █████╗ ██╗  ██╗███████╗██████╗ 
    ██║████╗  ██║██╔════╝██╔═══██╗    ██║     ██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██║██╔██╗ ██║█████╗  ██║   ██║    ██║     █████╗  ███████║█████╔╝ █████╗  ██████╔╝
    ██║██║╚██╗██║██╔══╝  ██║   ██║    ██║     ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║██║ ╚████║██║     ╚██████╔╝    ███████╗███████╗██║  ██║██║  ██╗███████╗██║  ██║
    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                       
             
                                                                                          
    """  + END+BLUE+'Sacia Info Leaker'.format(BLUE, END).center(69) +
    '\n' + '\tMade by: {}Sacia'.format(BLUE, BLUE).center(76) +
'\n' + '\tVersion: {}2.0{}\n'.format(BLUE, END).center(80) + '\n')

space = '\n'
info = input(BLUE+"\nPaste info here!:   ")
file = open('info.txt', 'a')
file.write(info)
file.close()
print(BLUE+"leaking info to database!")

system('git add .')
system('git commit -m "info"')
system('git push -f origin master')
system('cls')
print(RED+"Info Is now public!")
time.sleep(100)

