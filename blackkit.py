#!/usr/bin/python3
# Created by inc0gnit0
# Idea by cracked.keys



# Dependencies
import hashlib
import os

# Setup
class colors:
    black = '\033[30m'
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    
    end = '\033[0m'

    bold = '\033[1m'
    underline = '\033[4m'
    blink = '\033[5m'

    back_white = '\033[47m'

# Main
# Code
# Hash code
def hash_str(h, t):
    # Long live if
    if t == "sha256":
        hashed = hashlib.sha256(h.encode('utf-8')).hexdigest()
        print(f"{colors.green}" + hashed)
        return 'Success'
    else:
        print(f"{colors.fail}ERROR: Hash is not supported.{colors.end}")
        os._exit(1)

# Prompts
# Prompt for tool
print(f"""{colors.back_white}{colors.black}{colors.bold}
  ____  _            _    _  ___ _   
 | __ )| | __ _  ___| | _| |/ (_) |_ 
 |  _ \| |/ _` |/ __| |/ / ' /| | __|
 | |_) | | (_| | (__|   <| . \| | |_ 
 |____/|_|\__,_|\___|_|\_\_|\_\_|\__|
 {colors.end}
""")
print("Welcome to BlackKit!")
try:
    tool = str(input("$ "))
except KeyboardInterrupt:
    print(f"\n{colors.fail}Exiting...{colors.end}")
    # Cleanup code
    print(f"{colors.end}")

    os._exit(0)

# Create a Python switch case
def switch(x):
    return {
        'hash': hash_str(str(input("String to be hashed: ")), str(input("Hash method (currently support sha256): ")))
    }.get(x, -1)

print(switch(tool))

