import subprocess
import sys
import time
import random
import os 
from colorstatscode import code


banner = """

casino work bot - by @slomay
"""
print(code.PURPLE, banner)
time.sleep(1) 
casino = subprocess.Popen([sys.executable, 'casino.py'])
print(code.STRT, '- casino bot')
time.sleep(1) 
ticket = subprocess.Popen([sys.executable, 'ticket.py'])
print(code.STRT, '- worker bot')

