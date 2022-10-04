#!/usr/bin/env python3
"""Alta3 Research"""

# standard library imports
import os
import zipfile

# function to search for all files within a directory and add them to our ZIP
def zipdir(dirpath, zipfileobj):
    """does the work of writing data into our zipfile"""
    # os.walk() returns a 3-tuple
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            print(os.path.join(root, file))
            zipfileobj.write(os.path.join(root, file))
        return None

def main():
    """called at runtime"""
    # ask the user for the directory to be archive
    dirpath = input("What directory are we archiving today? ")

    # if the directory exists can begin archiving
    if os.path.isdir(dirpath):
        zippedfn = input("What should we call the finished archive? ")
        ## zippedfn is the zipped file for the archive
        with zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) as zipfileobj:
            zipdir(dirpath, zipfileobj)

    else:
        print("Run the script again when you have a valid directory to zip.")

# call the main function
main()
