#!/usr/bin/python3

import sys
import os
import time

if len(sys.argv) == 2:
    try:
        minutes = int(sys.argv[1])
        seconds = minutes*60
    except:
        print("!!Error!!Please Pass Time as Integer Value")
        exit(2)
else:
    print("Usage: break.py minutes")
    exit(2)

for sec in range(seconds):
    os.system('clear')
    print("\n\n\n\n\n")
    print(f"Time Left {seconds-sec}".center(100))
    print("\n\n\n\n")
    time.sleep(1)

