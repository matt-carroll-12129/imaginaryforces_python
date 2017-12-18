# Fonts downloaded from TypeKit and one of our clients were all hidden ("." before filename).
# This script removes the leading dot and unhides them. 
# Change the variable hidden_font_path for use. 
# Written by Matt Carroll


import os

hidden_font_path = "/Users/matt.carroll/Desktop/Fonts/"

for directname, directnames, files in os.walk(hidden_font_path):
    for file in files:
        # Split the file into the filename / extension
        filename, ext = os.path.splitext(file)
        if "." in filename:
            # If '.' is in the filename, rename to remove '.'
            new_name = filename.replace(".", "")
            os.rename(os.path.join(directname, file), os.path.join(directname, new_name + ext))