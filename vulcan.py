#!/usr/bin/env python3

from subprocess import check_output
from sys import platform
import pprint
# Step Group 1: Safety checks
print("Performing OS and safety checks...")

# Step1.1: Check for linux environment
#TODO: Remove darwin once finished prototyping
accepted_os = ["linux", "darwin"]

if platform not in accepted_os:
    print("Your OS is currently not supported. Exiting...")
    exit(99)
else:
    print("OS Check: PASS (%s)" % (platform))

# Step1.2: Check for boot device, and ban it from ever being touched
#Only works for linux for now
boot_devices = ["/boot", "/System/Volumes/Data"]
df = check_output(['df']).decode()
dflines = df.split('\n')

for line in dflines:
    for item in boot_devices:
        if item in line:
          print(line)
        else:
          pass
"""
pprint.pprint(dflines)
print(type(dflines))
"""


