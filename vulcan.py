#!/usr/bin/env python3

from safety_check import safety_check
from pprint import pprint as print
from glob import glob
import threading
import inquirer
import os
from dd import dd

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
        inquirer.Checkbox('devices',
            message="What disks would you like to format?",
            choices=safe_pruned_devs,
            ),
        inquirer.List('format_type',
            message="Choose dd data type", 
            choices=["Random (slower, more secure)", "Zero (Faster, probably)"]),
        inquirer.Confirm('confirm',
            message='Confirm deletion of the above drives?',
            default=False,)
        ]

answers = inquirer.prompt(questions)
dd_devices = answers[devices]
dd_data = answers[format_type]
dd_conf = answers[confirm]



print(answers)

