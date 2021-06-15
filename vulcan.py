#!/usr/bin/env python3

from safety_check import safety_check
from glob import glob
from pprint import pprint as print
import os
import inquirer

# Checks for OS and Boot device, called from ./safety_check.py
safety_check()

# Step 2.1: List all available drives
supported_proto = ["sd", "nvme"]

dev_path = "/dev"
safe_pruned_devs = []
for proto in supported_proto:
    for dev in glob('%s/%s*' % (dev_path, proto)):
        if safety_check.boot_device not in dev:
            safe_pruned_devs.append(dev)

#Sets up the checkbox menu
questions = [
        inquirer.Checkbox('Devices',
            message="What disks would you like to format?",
            choices=safe_pruned_devs,
            ),
        ]

#this spits out a dict
answers = inquirer.prompt(questions)





