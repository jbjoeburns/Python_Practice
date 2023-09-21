import os

# asks user where they want the file to be made
# adds \new_folder at the end of specified location, as that is what we want to name the new folder
desired_location = input("Please specify where you would like the directory to be made: ") + "\\new_folder"

# makes new folder at this location
os.mkdir(desired_location)