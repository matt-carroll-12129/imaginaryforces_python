# If a Cinema license.ini file does not exist this script creates one and points to a valid license server.
# If a file does exist it will overwrite it with the correct license server address. 
# Written by Matt Carroll



import os

o = open("C:\Program Files\MAXON\CINEMA 4D R17\license.ini", "w")

o.write("[settings]\n")
o.write("server = license-awswest-1\n")
o.write("port = 5235")
o.close()

# removed r16