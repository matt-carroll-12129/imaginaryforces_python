## This script iterates over all current users ~/Library folder and replaces userSetup.mel file with updated version.
## This is part of a larger package I created which places usersetup.mel file in the /tmp directory. 
## written by Matt Carroll 


import os
import shutil 

for user in os.listdir('/Users'):
	 
	path_to_script_directory = os.path.join('/Users', user, 'Library/Preferences/Autodesk/maya/scripts')
	path_to_script = os.path.join('/Users', user, 'Library/Preferences/Autodesk/maya/scripts/userSetup.mel')
	 
	if os.path.isfile(path_to_script):
		os.remove(path_to_script)

	if os.path.isdir(path_to_script_directory):
		shutil.copy('/tmp/userSetup.mel', path_to_script_directory)	 	






