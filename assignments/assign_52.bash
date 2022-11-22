
# assignment 52

####################################################################
# this assignment is NOT clear about how it is to be submitted to
# Gradescope -- i.e., is it to be submited as a bash script file or
# are you supposed to submit just the number .py files found?
#
# If this assignment is supposed to be submitted as a bash script
# file, then all the text below is what should be included in the
# bash script file
####################################################################


#!/bin/bash

# clone CS class's repo from GitHub into your hard drive
git clone https://github.com/HunterCSci127/CSci127

# change to the created repo directory and make a directory called 'projects'
cd CSci127
mkdir projects

# move averageImage.py into 'projects' directory
mv averageImage.py projects

# change to the repo directory and make another directory called 'pictures'
cd CSci127	# this command is really not necessary b/c you are already in this directory
mkdir pictures

# move all .png files in the repo directory into the 'pictures' directory
# (use the * wildcard to take the place of all possible names)
mv *.png pictures

# find out the number of files ending in '.py' in the repo directory
# (use 'grep' to search and use 'pipe' to transfer the results to the next command)
ls -l | grep ".py" | wc -l

# there are 24 .py files
