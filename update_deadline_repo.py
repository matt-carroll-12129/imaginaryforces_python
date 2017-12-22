# I created a new deadline_repo for Deadline8. The windows nodes look for this repo using the 
# deadline.ini file. This script removes the old file and replaces with updated version.
# Written by Matt Carroll

import os
import shutil

## Remove deadline config file
os.remove("C:\ProgramData\Thinkbox\Deadline8\deadline.ini")

## Copy NY Repository config file from Server to destination 
shutil.copy("T:\_Systems\matt\deadline.ini", "C:\ProgramData\Thinkbox\Deadline8")