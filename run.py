#!/usr/bin/env python3

import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('command', help="write command to run")

args = parser.parse_args()

status, op = subprocess.getstatusoutput(args.command)

if status == 0:
    print(op)
else:
    print("Error!!!", op)
