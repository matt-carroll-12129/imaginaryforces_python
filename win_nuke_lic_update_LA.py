# When we updated our Nuke licenses The Foundry asked that we move from FLexLM to RLM.
# This script deletes the old license file from Nuke's FlexLM directory and copies a new
# one to the RLM directory on all render nodes. 


import os 
import shutil

## Remove old FLEXLM license files. 

pathFLEXfolder1 = "C:/Program Files/The Foundry/FLEXlm"
fileList = os.listdir(pathFLEXfolder1)
for fileName in fileList:
	os.remove(pathFLEXfolder1+ "/" + fileName)


## Copy the client .lic file into RLM folder. This points client to new server.

if not os.path.exists("C:/Program Files/The Foundry/RLM/foundry_client.lic"):
	shutil.copy("Z:/_Systems/floating_lics/foundry_client.lic", "C:/Program Files/The Foundry/RLM/")

