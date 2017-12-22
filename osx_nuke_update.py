# This removes all license files from the FLEXlm directory and copies a new file to the RLM directory for Nuke.
# Must be run with elevated permissions. 
# Written by Matt Carroll

import os 
import shutil

## Remove FLEXLM files from 2 locations
pathFLEXfolder = "/Library/Application Support/TheFoundry/FLEXlm"
if os.path.exists(pathFLEXfolder):
	fileList = os.listdir(pathFLEXfolder)
	for fileName in fileList:
		os.remove(pathFLEXfolder + "/" + fileName)


## Ensure the RLM directory exists. If it does not, create one. 
if not os.path.exists("/Library/Application Support/TheFoundry/RLM"):
	os.makedirs("/Library/Application Support/TheFoundry/RLM")

## Copy the client .lic file into RLM folder. This points client to primary and failover server
if not os.path.exists("/Library/Application Support/TheFoundry/RLM/foundry_client.lic"):
	shutil.copy("/Romulus/romulus/_Systems/licenses/nuke/for_client/foundry_client.lic", "/Library/Application Support/TheFoundry/RLM/")

