# This is function but could use some polishing. It is for my own use to swap Nuke file paths and is not out in production. It is meant to be run from command line and takes inputs of 
# a nuke file directory and nuke file name. It will create a new file in which paths are swapped from unix to Windows.
# The new file has "_windows.nk" added to the end. 
# Written by Matt Carroll

import os 
import string
import shutil 

nuke_filedir = raw_input('What is the path to your directory?')
nuke_filename = raw_input('what is your filename?')

os.chdir(nuke_filedir)
new_filename = nuke_filename + '_windows.nk'


p1 = open(nuke_filename, 'r')
p2 = open(new_filename, 'w')
for line in p1:
	p2.write(line.replace('/Romulus/romulus/', 'T:\\'))


