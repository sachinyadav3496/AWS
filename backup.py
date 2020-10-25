#!/usr/bin/env python3

"""
    A Backup Scripts to take backup of Directories

    Exit Status:
        0 - Sucess
        2 - Error in file copy
        3 - Permission Error
        4 - Path are not directories
        5 - Path does not exists
"""
import argparse
import subprocess
import os

# os.system('cmd') --> status code

parser = argparse.ArgumentParser()
parser.add_argument('src', help='source directory to be backupped')
parser.add_argument('dest', help='destination directory where backups are stored')
args = parser.parse_args()

src = args.src
dest = args.dest
if os.path.exists(src) and os.path.exists(dest):
    if os.path.isdir(src) and os.path.isdir(dest):
        if os.access(src, os.R_OK) and os.access(dest, os.W_OK):
            date = "_" + subprocess.getoutput("date +'_%d_%m_%Y_%s'")
            src = src.rstrip('/')
            dir_name = src.split('/')[-1]
            path = os.path.join(dest, dir_name+date)
            command = f"cp -r {src} {path}"
            status, output = subprocess.getstatusoutput(command)
            if status == 0:
                print("...............Backup Sucessfull...............")
                exit(0)
            else:
                print(f"___Error!!! {output}___")
                exit(2)
        else:
            print("!!Error!! You do not have enough permission to perform this task")
            exit(3)
    else:
        print("!!Error!! We only Backup Directories not Files Check Path Try Again")
        exit(4)
else:
    print("Error!! Please Double Check you path parameters Beacuse They do not exists")
    exit(5)

