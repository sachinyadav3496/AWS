#!/usr/bin/env python3
"""
    hello script to greet user

    usage hello.py name [-u/--uper]

    exit status:
        0 sucess
        2 Error argument error
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('name', type=str, help="Please Pass your Name")

parser.add_argument('--upper','-u',  action='store_true')

args = parser.parse_args()

if args.upper:
    name = args.name.upper()
else:
    name = args.name

print("Welcome user: ", name)


exit(0)
