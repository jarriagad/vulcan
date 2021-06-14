#!/usr/bin/env python3

from subprocess import check_output
from sys import platform

# Step Group 1: Safety checks
print("Performing OS and safety checks...\n")

# Step1.1: Check for linux environment
#TODO: Remove darwin once finished prototyping
accepted_os = ["linux", "darwin"]

if platform not in accepted_os:
    print("Your OS is currently not supported. Exiting...")
    exit(99)

# Step1.2: Check for boot device, and ban it from ever being touched
#Only works for linux for now
df = check_output(['df']).decode()
dflines = df.split('\n')
for line in dflines:
        if '/boot' in line:
                print(line.split(' ')[0])



