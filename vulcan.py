#!/usr/bin/env python3

from subprocess import check_output
from sys import platform

# Step Group 1: Safety checks
print("Performing OS and safety checks...")

# Step1.1: Check for linux environment
accepted_os = ["linux", "darwin"]

if platform not in accepted_os:
    print("Your OS is currently not supported. Exiting...")
    exit(99)
else:
    print("OS Check: PASS (%s)" % (platform))

# Step1.2: Check for boot device, and ban it from ever being touched
boot_devices = ["/boot", "/System/Volumes/Preboot"]
df = check_output(['df']).decode()
dflines = df.split('\n')

for line in dflines:
    for item in boot_devices:
        if item in line:
          boot_partition = line.split()[0]
          if item == boot_devices[0]:
            boot_device = boot_partition[:-1]
          if item == boot_devices[1]:
            boot_device = boot_partition[:-2]
          print("Boot device Check: PASS (%s)" % (boot_device))
        else:
          pass


