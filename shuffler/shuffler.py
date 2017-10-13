#!/bin/python
#
# shuffler.py: Finds all of the music files in the selected folder, scrambles the names and 
# puts them all into one folder for play by car adapter without shuffle. This script will flatten
# directories in the input parameter directory.
#
# This is a shuffling method for my car.
#
# Execution: python shuffler.py FOLDER_NAME

import os
import string
import sys
import shutil
import random
import math

# Constants
HOME_FOLDER = os.getcwd()

def main ():
    fileNames = [];
    
    # Grab the folder full of music
    print "Hello, this program shuffles file names.\n"
    folder = sys.argv [1]
    
    # Set up the landing point for files
    dest = HOME_FOLDER + "/shuffle/"
    if os.path.exists(dest) == True:
        shutil.rmtree(dest)
    
    os.mkdir(dest)
        
    
    # Recursively grab the files
    fileNames = getFiles ("", folder);
    print "\nGot all files..."
    random.shuffle(fileNames)
    
    index = 1
    # Change the names of the files and move them. This is done to reflect the
        # newly shuffled order. NOTE: The files will still have their metadata attached
    for fileName in fileNames:
        os.rename(fileName, dest + getZeroString(len(fileNames), index) + ".mp3")
        index += 1
        
    print "DONE!!!"
        
# Adds leading zeroes if number is small.
def getZeroString (numFiles, number):
    returnString = ""
    for i in range (int(math.log10(numFiles))+1 - int(math.log10(number))+1):
        returnString += "0"

    returnString += str(number)
    return returnString

# Recursively grabs all of the files from the specific folder
#
# Base case: There are no folders in the homeFolder, return the list of files
# Recursive case: There is another folder in the homeFolder,
#       then go a level deeper, and extend the list returned from it.
def getFiles (homeFolder, folderName):

    fileNames = []
    
    # Go into that directory
    os.chdir(folderName)
    
    # Make sure the file name format is consistent and correct.
    if folderName[-1] != "/":
        folderName += "/"
    
    # For each on the list of files in the current directory
    for files in os.listdir("."):
        if files.endswith(".mp3"):
            fileNames.append(homeFolder + folderName + files)
            print ".",
            
        elif os.path.isdir(files):
            print "*",
            fileNames.extend(getFiles(homeFolder + folderName, files))
    
    # Return to the original folder so that we will end where we began this loop
    os.chdir(HOME_FOLDER)
    return fileNames
    
main()
