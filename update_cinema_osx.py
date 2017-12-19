# Munki has replaced the need for this script, but it should still be kept around for reference. 
# This overwrites the license.ini file in the r17 directory to point to our "new" license server. 
# If license.ini does not exist then the script will create it. 

import os

o = open("/Applications/MAXON/CINEMA 4D R17/license.ini", "w")

o.write("[settings]\n")
o.write("server = license-awswest-1\n")
o.write("port = 5235")
o.close()

