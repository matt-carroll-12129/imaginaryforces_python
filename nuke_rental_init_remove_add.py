# This was a quick fix for rental machines that came in before the Munki workflow was established. First an init.py file is dropped 
# into /tmp via ARD. This script checks to see if an init.py file already exists. If it does, it is deleted (outdated). The script also 
# ensures the ~/.nuke folder exists for all users and creates one if it does not. Then it copies the correct init.py file from /tmp to each
# users ~/.nuke directory. 


import os
import shutil 

for user in os.listdir('/Users'):
	 
	path_to_nuke_directory = os.path.join('/Users', user, '.nuke')
	path_to_init_file = os.path.join('/Users', user, '.nuke/init.py')
	 
	if os.path.isfile(path_to_init_file):
		os.remove(path_to_init_file)

	if not os.path.exists(path_to_nuke_directory):
		try:
			os.chdir(os.path.join('/Users', user))
			os.makedirs('.nuke', 0777)
			os.chmod('.nuke', 0777)
		except OSError:
			pass



	if os.path.isdir(path_to_nuke_directory):
		shutil.copy('/tmp/init.py', path_to_nuke_directory)	
		






